# SanchAI Analytics – Weather Query Assistant

**Internship Technical Assessment Submission**

A minimal, clean, and assignment-focused full-stack application that allows users to ask **weather-related questions for any city** using natural language.

This project demonstrates **LLM-based tool orchestration** using **LangChain**, with a **FastAPI backend** and a **React frontend**.

---

## Assignment Objective

Build a web application where:

* Users can ask questions like *“What’s the weather in Pune?”*
* The backend uses an **LLM with a tool** to fetch weather data
* The frontend displays the generated response
* Non-weather queries are handled gracefully

This project strictly follows the scope provided in the assignment.

---

## Core Concept

The backend is powered by a **LangChain Agent** that:

* Interprets the user’s natural language query
* Decides whether a weather tool should be invoked
* Calls the OpenWeather API via a tool when required
* Returns a human-readable response to the frontend

There is:

* ❌ No manual keyword detection
* ❌ No regex-based city extraction
* ❌ No hard-coded business logic

All reasoning and decision-making is handled by the **LLM agent**.

---

## Architecture Overview

```
User (React UI)
   ↓
FastAPI Backend
   ↓
LangChain Agent (via OpenRouter LLM)
   ↓
Weather Tool (OpenWeather API)
   ↓
Final Response to Frontend
```

---

## Application Screenshots

### Weather Query Example

User asks a valid weather-related question and receives real-time weather data.

<img width="1913" height="872" alt="image" src="https://github.com/user-attachments/assets/e7732120-0235-4d89-a867-a231c8538579" />


<!-- <img width="1917" height="871" alt="Weather Query Example" src="https://github.com/user-attachments/assets/1d805c67-046a-429b-bc9e-cdbb4bf50b8e" /> -->

---

### Non-Weather Query Handling

If the user asks something unrelated, the agent politely explains that it only supports weather queries.
<img width="1916" height="873" alt="image" src="https://github.com/user-attachments/assets/1a11095a-c6d4-489b-9c86-ea2111bfb499" />

<!-- <img width="1330" height="862" alt="Non Weather Query" src="https://github.com/user-attachments/assets/d0b8a468-5e77-454d-b935-520f237d1bcb" /> -->

---

## Technology Stack

### Frontend

* React
* JavaScript
* Fetch API

### Backend

* FastAPI
* LangChain (Agents + Tool Calling)
* OpenRouter (LLM Provider)
* OpenWeather API

---

## Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DurgeshSakhare23/Sanchai_Analytics_Assignment.git
cd Sanchai_Analytics_Assignment
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file inside the **backend** folder:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Run the backend server:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## Example API Usage

### Request

```http
POST /chat
Content-Type: application/json

{
  "message": "Tell me the weather in Nagpur"
}
```

### Response

```json
"The weather in Nagpur is haze. Temperature: 18°C, Humidity: 59%."
```

---

## Author

**Durgesh Sakhare**
B.Tech Student
Backend & AI-Focused Developer
