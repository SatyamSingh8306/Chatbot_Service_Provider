import streamlit as st
import requests
from typing import Dict, Any

# Constants
API_BASE_URL = "http://localhost:8000"
API_ENDPOINTS = {
    "health": f"{API_BASE_URL}/api/",
    "chat": f"{API_BASE_URL}/api/chat",
}

def send_message(message: str) -> Dict[str, Any]:
    """Send a message to the chat API."""
    try:
        response = requests.post(API_ENDPOINTS["chat"], json={"message": message})
        return response.json()
    except requests.exceptions.RequestException:
        return {"status": "error", "message": "Failed to send message"}

def main():
    st.set_page_config(
        page_title="ImReadyAI Chatbot",
        page_icon="🤖",
        layout="centered"
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("🤖 ImReadyAI Chatbot")

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = send_message(prompt)
                if response:
                    bot_response = response.get("response", "I apologize, but I couldn't process your request.")
                    st.write(bot_response)
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": bot_response})
                else:
                    st.error("Failed to get a response from the API")

if __name__ == "__main__":
    main() 