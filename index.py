from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Serve the HTML file
@app.route('/')
def serve_html():
    return send_from_directory(os.path.abspath('.'), 'main.html')

# WebSocket message handling
@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")  # Log messages on the server console
    send(message, broadcast=True)  # Broadcast message to all clients

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
