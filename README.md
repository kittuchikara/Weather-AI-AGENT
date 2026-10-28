## 🌦️ Weather AI Agent

An AI-powered weather assistant built using Python, Groq, Open-Meteo API, and Streamlit. It retrieves live weather information for cities around the world and allows users to compare weather conditions across multiple locations through natural language queries.

The application uses LLM-based tool calling to understand user requests, execute Python weather functions, retrieve actual weather data, and generate conversational responses.

# 🚀 Features
* Live Weather Information: Retrieve current temperature, weather conditions, and wind speed for cities worldwide.
* Multi-City Weather Comparison: Compare current weather conditions between multiple cities.
* AI Tool Calling: Uses Groq LLMs to identify when weather tools should be executed.
* Open-Meteo Integration: Fetches weather data using Open-Meteo's geocoding and forecast APIs.
* Natural Language Interaction: Ask weather-related questions using a conversational interface.
* Jinja Prompt Templates: Dynamically generate system prompts and tool descriptions.
* Modular Architecture: Separate modules for agent logic, configuration, prompts, schemas, and weather tools.
* Streamlit Chat Interface: Interactive chat interface with conversation history.
* Cloud Deployment: Deployed using Streamlit Community Cloud.

# 🧠 How It Works

1.The application follows an LLM-based tool-calling workflow.
2.The user submits a weather-related query through the Streamlit interface.
3.The query and system prompt are sent to the Groq language model.
4.The LLM determines whether a weather tool needs to be called.
5.If a tool call is requested, the Python agent executes the corresponding function.
6.The weather function retrieves location coordinates using the Open-Meteo Geocoding API.
7.The function requests current weather information from the Open-Meteo Forecast API.
8.The actual weather result is returned to the LLM.
9.The LLM generates a concise, natural-language response for the user.

# 🛠️ Tech Stack

Python | Groq | Qwen | Open-Meteo API | Streamlit | Jinja2 | GitHub | Requests 

# Agent Workflow

User Query
    ↓
Streamlit Chat Interface
    ↓
Groq LLM
    ↓
Tool Calling Decision
    ↓
Python Agent
    ↓
Weather Tool
    ↓
Open-Meteo API
    ↓
Weather Data
    ↓
LLM Generates Response
    ↓
Streamlit Displays Answer

## ⚙️ Installation and Setup

# 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/Weather-AI-AGENT.git

Navigate to the project directory:

cd Weather-AI-AGENT

# 2. Create a Virtual Environment

python -m venv venv3

Activate the virtual environment.

Windows:

venv3\Scripts\activate

Git Bash:

source venv3/Scripts/activate

# 3. Install Dependencies

pip install -r requirements.txt

# 4. Configure Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=your_groq_api_key

GEOCODE_URL=https://geocoding-api.open-meteo.com/v1/search

FORECAST_URL=https://api.open-meteo.com/v1/forecast

WEATHER_REQUEST_TIMEOUT=10

MAX_TURNS=10

MAX_TOKENS=4096

Replace your_groq_api_key with your actual Groq API key.

Important: Never upload your .env file or expose your API key publicly.

Open-Meteo's standard weather endpoints do not require an API key for typical usage.

# 5. Run the Application

streamlit run app.py

The application will open in your browser.

# 🌐 Deployment
Deployed using Streamlit Community Cloud.
# Live link-> https://weather-ai-agent-8czu5rpjsql9gkmzsrhtkm.streamlit.app/
