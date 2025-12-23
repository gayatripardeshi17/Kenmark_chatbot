# Kenmark ITan Solutions Chatbot

## Setup Instructions

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Get Gemini API Key:
   - Go to https://makersuite.google.com/app/apikey
   - Create a new API key
   - Replace "YOUR_GEMINI_API_KEY" in app.py with your actual key

3. Prepare Excel file:
   - Use knowledge_base.xlsx or create your own
   - Format: Category | Question | Answer

4. Run the application:
   ```
   python app.py
   ```

5. Open browser and go to: http://localhost:5000

## Excel File Format

Your Excel file should have these columns:
- Category: Type of question (About, Services, Contact, etc.)
- Question: The question users might ask
- Answer: The response to provide

## Features

- AI-powered responses using Gemini API
- Excel-based knowledge management
- Clean, responsive web interface
- Real-time chat experience