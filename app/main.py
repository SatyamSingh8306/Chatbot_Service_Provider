"""
Main application module for ImReadyAI Chatbot
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config.settings import ALLOWED_ORIGINS, PORT
from app.routers import chat_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="ImReadyAI Chatbot",
    description="Intelligent chatbot for ImReadyAI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route handler
@app.get("/")
async def root():
    """Root endpoint that provides API information"""
    return JSONResponse({
        "message": "Welcome to ImReadyAI Chatbot API",
        "documentation": "/docs",
        "api_endpoints": {
            "health_check": "/api/",
            "chat": "/api/chat",
            "sessions": "/api/chat/sessions"
        },
        "status": "running"
    })

# Include routers
app.include_router(chat_router, prefix="/api") 