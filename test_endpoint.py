import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app=app)

def test_health_endpoint():
    response = client.get('/api/')
    assert response.status_code == 200
    assert response.json() == {"message": "ImReadyAI Chatbot API is running", "status": "healthy"}

def test_root_endpoint():
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert "api_endpoints" in data
    assert "documentation" in data

def test_chat_endpoint():
    # Test chat endpoint with valid input
    response = client.post(
        '/api/chat',
        json={
            "message": "Hello",
            "session_id": "test-session"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "session_id" in data

def test_sessions_endpoint():
    # Test getting sessions
    response = client.get('/api/chat/sessions')
    assert response.status_code == 200
    data = response.json()
    assert "active_sessions" in data
    assert "total_sessions" in data
    assert isinstance(data["active_sessions"], list)

    # Test clearing all sessions
    response = client.delete('/api/chat/sessions')
    assert response.status_code == 200
    assert response.json() == {"message": "All sessions cleared successfully"}

def test_specific_session_endpoint():
    # Test clearing specific session
    session_id = "test-session"
    response = client.delete(f'/api/chat/session/{session_id}')
    assert response.status_code == 200
    assert response.json() == {"message": f"Session {session_id} not found"}

if __name__ == '__main__':
    pytest.main([__file__, "-v"])
