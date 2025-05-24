# ImReadyAI Chatbot

A modern, intelligent chatbot powered by Groq's LLM technology, built with FastAPI and Python.

## Features

- 🤖 Advanced AI-powered conversations
- 🔄 Session management for continuous conversations
- 🚀 Fast and efficient API endpoints
- 🔒 Secure and scalable architecture
- 📝 Comprehensive API documentation

## Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerized deployment)
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/imreadyai-chatbot.git
cd imreadyai-chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your configuration:
```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.1-70b-versatile
TEMPERATURE=0.7
MAX_TOKENS=1024
PORT=8000
```

## Running the Application

### Local Development

1. Start the application:
```bash
./start.sh
```

2. Access the API at `http://localhost:8000`

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t imreadyai-chatbot .
```

2. Run the container:
```bash
docker run -p 8000:8000 --env-file .env imreadyai-chatbot
```

## API Endpoints

- `GET /`: Root endpoint with API information
- `GET /api/`: Health check endpoint
- `POST /api/chat`: Main chat endpoint
- `GET /api/chat/sessions`: List active sessions
- `DELETE /api/chat/sessions`: Clear all sessions
- `DELETE /api/chat/session/{session_id}`: Clear specific session

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
app/
├── __init__.py
├── __main__.py           # Entry point
├── dependencies.py       # Shared dependencies
├── main.py              # Main application
├── routers/             # API routes
│   ├── __init__.py
│   └── chat.py          # Chat-related routes
├── services/            # Business logic
│   ├── __init__.py
│   └── chat.py          # Chat service
├── types/               # Type definitions
│   ├── __init__.py
│   └── chat.py          # Chat-related types
└── utils/               # Utility functions
    ├── __init__.py
    └── errors/          # Error handling
```

## Development

### Running Tests

```bash
pytest
```