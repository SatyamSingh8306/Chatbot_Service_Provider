if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Set default values if not in .env
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}
export ENV=${ENV:-production}

echo "Starting ImReadyAI Chatbot API..."
echo "Available endpoints:"
echo "- Root: http://localhost:8000/"
echo "- Health check: http://localhost:8000/api/"
echo "- Chat: http://localhost:8000/api/chat"
echo "- Sessions: http://localhost:8000/api/chat/sessions"
echo "- API Documentation: http://localhost:8000/docs"
echo "Press Ctrl+C to stop the server"
echo ""

# Run the application
python -m app