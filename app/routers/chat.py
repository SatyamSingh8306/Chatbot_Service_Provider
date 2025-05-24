import logging
import asyncio
import traceback
from fastapi import APIRouter, HTTPException, Depends
from app.types.chat import ChatRequest, ChatResponse
from app.dependencies import get_llm_manager

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "ImReadyAI Chatbot API is running", "status": "healthy"}

@router.get("/health")
async def health_check(llm_manager=Depends(get_llm_manager)):
    """Detailed health check"""
    sessions = llm_manager.get_active_sessions()
    return {
        "status": "healthy",
        "active_sessions": sessions["total_sessions"]
    }

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    llm_manager=Depends(get_llm_manager)
):
    """Main chat endpoint"""
    try:
        logger.info(f"Received chat request: {request.message[:50]}... (session: {request.session_id})")
        
        # Get or create conversation session
        session_chain = llm_manager.get_or_create_session(request.session_id)
        logger.info(f"Using session: {request.session_id}")
        
        # Get response from the conversation chain
        logger.info("Calling Groq API...")
        response = await asyncio.to_thread(
            session_chain.predict,
            input=request.message
        )
        logger.info(f"Got response: {response[:100]}...")
        
        return ChatResponse(
            response=response,
            session_id=request.session_id
        )
    
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

@router.delete("/chat/session/{session_id}")
async def clear_session(
    session_id: str,
    llm_manager=Depends(get_llm_manager)
):
    """Clear a specific chat session"""
    if llm_manager.clear_session(session_id):
        return {"message": f"Session {session_id} cleared successfully"}
    return {"message": f"Session {session_id} not found"}

@router.delete("/chat/sessions")
async def clear_all_sessions(llm_manager=Depends(get_llm_manager)):
    """Clear all chat sessions"""
    llm_manager.clear_all_sessions()
    return {"message": "All sessions cleared successfully"}

@router.get("/chat/sessions")
async def get_active_sessions(llm_manager=Depends(get_llm_manager)):
    """Get list of active sessions"""
    return llm_manager.get_active_sessions() 