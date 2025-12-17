# Weather Query Application

A minimal web application with React frontend and FastAPI backend that uses Langchain + OpenRouter to answer weather queries.

## Features

- **React Frontend**: Clean and modern UI with input box and send button
- **FastAPI Backend**: Fast and efficient API server
- **Langchain Integration**: Uses Langchain agents with OpenRouter LLM
- **Weather Tool**: Custom tool to fetch real-time weather data
- **Natural Language Processing**: Ask weather questions in natural language

## Project Structure

```
.
├── backend/
│   ├── main.py              # FastAPI application with Langchain agent
│   ├── requirements.txt     # Python dependencies
│   └── .env.example        # Environment variables template
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Styling
│   │   ├── index.js        # React entry point
│   │   └── index.css       # Global styles
│   └── package.json        # Node dependencies
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 16+
- OpenRouter API key (get from https://openrouter.ai/)
- OpenWeather API key (optional, get from https://openweathermap.org/api)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file from the example:
   ```bash
   copy .env.example .env
   ```

6. Edit `.env` and add your API keys:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   ```

7. Run the backend server:
   ```bash
   python main.py
   ```

   The backend will start on http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

   The frontend will open at http://localhost:3000

## Usage

1. Ensure both backend and frontend servers are running
2. Open http://localhost:3000 in your browser
3. Type a weather query like:
   - "What's the weather in Pune?"
   - "How's the weather in London today?"
   - "Tell me the weather of Tokyo"
4. Click the send button or press Enter
5. The AI assistant will process your query and return the weather information

## How It Works

1. **User Input**: User enters a natural language query in the React frontend
2. **API Request**: Frontend sends the query to the FastAPI backend
3. **Langchain Agent**: Backend uses Langchain agent with OpenRouter LLM to process the query
4. **Tool Invocation**: Agent identifies the need to check weather and calls the `get_weather` tool
5. **Weather Data**: Tool fetches real-time weather data from OpenWeather API
6. **Response Generation**: LLM generates a natural language response with the weather information
7. **Display**: Frontend displays the response to the user

## API Endpoints

### POST /query
Process a weather query

**Request Body:**
```json
{
  "query": "What's the weather in Pune?"
}
```

**Response:**
```json
{
  "response": "The weather in Pune is clear sky. Temperature: 24°C (feels like 23°C), Humidity: 45%"
}
```

### GET /
Health check endpoint

**Response:**
```json
{
  "message": "Weather Query API is running"
}
```

## Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Langchain**: Framework for building LLM applications
- **OpenRouter**: Access to various LLM models
- **OpenWeather API**: Real-time weather data

### Frontend
- **React**: JavaScript library for building user interfaces
- **Axios**: HTTP client for API requests
- **CSS3**: Modern styling with gradients and animations

## Notes

- The application uses `meta-llama/llama-3.1-8b-instruct:free` model from OpenRouter
- If OpenWeather API key is not provided, the weather tool returns placeholder data
- CORS is enabled for development (configure appropriately for production)

## License

MIT
