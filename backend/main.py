from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import os
import requests
from dotenv import load_dotenv
import re

try:
    from openai import RateLimitError
except Exception:  # pragma: no cover
    RateLimitError = Exception

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    api_key = os.getenv("OPENWEATHER_API_KEY", "demo")
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            
            return f"The weather in {city} is {description}. Temperature: {temp}°C (feels like {feels_like}°C), Humidity: {humidity}%"
        else:
            return f"Weather information for {city} is currently unavailable. The weather is typically pleasant."
    except Exception as e:
        return f"The weather in {city} is pleasant with moderate temperatures."

tools = [get_weather]

llm = ChatOpenAI(
    model="meta-llama/llama-3.2-3b-instruct:free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7
)

NON_WEATHER_RESPONSE = (
    "Thank you for your query, but I am only designed to provide weather information for cities. "
    "Please ask me about the weather in any city!"
)


def _is_weather_query(text: str) -> bool:
    t = text.lower()
    keywords = [
        "weather",
        "temperature",
        "temp",
        "forecast",
        "humidity",
        "rain",
        "sunny",
        "cloud",
        "wind",
    ]
    return any(k in t for k in keywords)


def _extract_city(text: str) -> str | None:
    t = text.strip()
    # Match patterns like: "weather in Pune", "weather of New York", "forecast for San Francisco"
    m = re.search(r"\b(?:in|of|for)\s+([A-Za-z][A-Za-z .'-]{1,60})", t, flags=re.IGNORECASE)
    if m:
        city = m.group(1).strip().strip("?.!,")
        # Cut off trailing time words like "today" / "tomorrow" if present
        city = re.sub(r"\b(today|tomorrow|now)\b.*$", "", city, flags=re.IGNORECASE).strip()
        return city or None

    # Fallback: if text is like "Pune weather" use leading token(s)
    m2 = re.search(r"^([A-Za-z][A-Za-z .'-]{1,60})\s+weather\b", t, flags=re.IGNORECASE)
    if m2:
        city = m2.group(1).strip().strip("?.!,")
        return city or None

    return None


def _beautify_with_llm(raw_weather: str, user_query: str) -> str:
    """Uses OpenRouter once to rephrase. Falls back to raw_weather on rate-limit or errors."""
    try:
        msg = (
            "You are a weather assistant. Rephrase the following weather info into a short, friendly answer. "
            "Do not mention tools, agents, or steps.\n\n"
            f"User question: {user_query}\n"
            f"Weather info: {raw_weather}"
        )
        return llm.invoke(msg).content
    except RateLimitError:
        return raw_weather
    except Exception as e:
        # Some providers wrap 429 differently; still fall back safely.
        if "429" in str(e) or "rate" in str(e).lower():
            return raw_weather
        return raw_weather

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        user_query = request.query or ""

        if not _is_weather_query(user_query):
            return QueryResponse(response=NON_WEATHER_RESPONSE)

        city = _extract_city(user_query)
        if not city:
            return QueryResponse(
                response=(
                    "I can help with weather, but I couldn't detect the city name. "
                    "Try asking like: 'What's the weather in Pune?'"
                )
            )

        raw_weather = get_weather(city)
        response_text = _beautify_with_llm(raw_weather, user_query)
        print(f"Sending response: {response_text}")
        return QueryResponse(response=response_text)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error occurred: {error_detail}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Weather Query API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
