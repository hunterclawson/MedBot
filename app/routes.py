from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db, bcrypt

from app.llm import get_user_query_response
from datetime import datetime
from flask import session
from flask import redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html') 

@main.route('/chat', methods=['GET', 'POST'])
@jwt_required(optional=True)  # Only require JWT for POST
def chat():
    if request.method == 'GET':
        # Render the chat page when accessed via GET
        return render_template('chat.html')
    
    # Process the POST request to handle chat messages
    data = request.get_json()
    
    if not data or 'query' not in data:
        return jsonify({'message': 'Invalid request: missing query'}), 400

    # Retrieve chat history from session or create a new one
    chat_history = session.get('chat_history', [])
    
    # Append the user query to the chat history
    chat_history.append({'role': 'user', 'content': data['query']})

    # Generate the response with the maintained chat history
    response = get_user_query_response(data['query'], chat_history)

    # Add AI's response to the chat history if available
    if response:
        chat_history.append({'role': 'assistant', 'content': response})
        session['chat_history'] = chat_history  # Update the session with the modified history
        return jsonify({'response': response})
    else:
        return jsonify({'message': 'Request could not be processed.'}), 500

