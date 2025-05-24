import logging
from typing import Dict
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from app.services.system_prompt import SYSTEM_PROMPT
from app.config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

logger = logging.getLogger(__name__)

class LLMManager:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )
        self.prompt_template = PromptTemplate(
            input_variables=["history", "input"],
            template=SYSTEM_PROMPT
        )
        self.conversation_sessions: Dict[str, ConversationChain] = {}
        logger.info("Successfully initialized Groq LLM")

    def get_or_create_session(self, session_id: str) -> ConversationChain:
        """Get existing session or create new one"""
        if session_id not in self.conversation_sessions:
            session_memory = ConversationBufferWindowMemory(k=10, return_messages=True)
            self.conversation_sessions[session_id] = ConversationChain(
                llm=self.llm,
                prompt=self.prompt_template,
                memory=session_memory,
                verbose=False
            )
        return self.conversation_sessions[session_id]

    def clear_session(self, session_id: str) -> bool:
        """Clear a specific chat session"""
        if session_id in self.conversation_sessions:
            del self.conversation_sessions[session_id]
            return True
        return False

    def clear_all_sessions(self):
        """Clear all chat sessions"""
        self.conversation_sessions.clear()

    def get_active_sessions(self):
        """Get list of active sessions"""
        return {
            "active_sessions": list(self.conversation_sessions.keys()),
            "total_sessions": len(self.conversation_sessions)
        } 