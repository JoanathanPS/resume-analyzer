# Resume Analyzer (FastAPI)

This is a basic FastAPI project that accepts resume files and returns a score, summary, and some feedback. It's designed to simulate how an AI might evaluate a resume (currently using mock logic).

### Features
- Upload a `.txt` resume
- Returns a mock score and feedback
- Built using FastAPI
- OpenAI/GPT support can be added later

### How to Run
1. Install the requirements:
pip install -r requirements.txt
2. Start the server:
uvicorn main:app --reload
3. Open your browser and go to:
http://127.0.0.1:8000/docs
You can test the API from there.

### Notes
This doesn't use real AI yet — it's just mocked logic for now. The idea is to demonstrate API building and basic backend flow. You can extend it later with OpenAI's API.
