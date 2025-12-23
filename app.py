import os
import pandas as pd
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from answer import get_answer

app = Flask(__name__)

# Configure Gemini API


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    print(f"Received message: {user_message}")  # Debug
    
    fallback_response = get_answer(user_message)
    return jsonify({'response': fallback_response})
    
   
if __name__ == '__main__':
    app.run(debug=True)