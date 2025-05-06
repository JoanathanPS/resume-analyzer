#AI-powered resume analyzer built with FastAPI
from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")
    
    # Mock analysis logic
    score = 82
    feedback = "Good structure. Add more specific achievements."
    summary = "Solid resume, but could benefit from quantified results."
    
    return {
        "score": score,
        "feedback": feedback,
        "summary": summary
    }

# Optional: for local testing
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
