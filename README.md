# Taskflow - Integrated AI Quick-Add Project

An assignment project featuring a FastAPI backend with an automated mock AI text parser to quickly create tasks.

## Features
- *POST /tasks/quick-add*: Accepts raw text and project ID, uses a rule-based mock LLM parser to extract priority and due date hints, and saves the task to the database.

## Deployment Setup on Render
- *Root Directory*: (Leave blank)
- *Build Command*: pip install -r requirements.txt
- *Start Command*: uvicorn backend.app.main:app --host 0.0.0.0 --port 10000
-