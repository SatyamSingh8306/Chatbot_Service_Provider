"""
Shared dependencies for the ImReadyAI Chatbot application
"""
from fastapi import Depends
from app.services.chat import LLMManager

def get_llm_manager() -> LLMManager:
    """Get LLM manager instance"""
    return LLMManager() 