    # MediGuide AI

MediGuide AI is an AI-powered medical information assistant designed to provide general health information while incorporating a safety-focused triage layer.

## Features

- AI-powered medical information assistant
- Safety and triage detection
- Emergency symptom detection
- Urgent symptom detection
- Caution-level symptom assessment
- Step-by-step symptom follow-up questions
- Medicine information lookup using MySQL
- Conversation history stored in MySQL
- Assessment results stored in the conversation history
- Groq-powered AI responses
- Flask REST API backend
- Environment-based configuration for API keys and database credentials

## Safety Architecture

MediGuide AI uses a layered safety flow:

User Message
      ↓
Safety / Triage Detection
      ↓
Emergency → Immediate medical-care guidance
      ↓
Urgent → Prompt professional assessment
      ↓
Caution → Follow-up symptom assessment
      ↓
Routine → Normal AI / medicine information flow

The system is designed to provide general educational information and is not intended to diagnose medical conditions or replace professional medical care.

## Tech Stack

- Python
- Flask
- Groq API
- MySQL
- mysql-connector-python
- HTML
- CSS
- JavaScript
- JSON
- Python virtual environment

## Project Structure

```text
MediGuide-AI/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── database.py
├── triage.py
├── red_flags.json
├── requirements.txt
├── .gitignore
└── README.md