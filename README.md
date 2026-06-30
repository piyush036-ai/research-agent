# ResearchMate – AI Research Agent
Built with IBM watsonx.ai + IBM Granite | AICTE IBM SkillsBuild 2026

---

## Setup (Local)

### 1. Get your IBM credentials
- Go to cloud.ibm.com → watsonx.ai → your project
- Copy your **API Key** (Manage → Access → API Keys)
- Copy your **Project ID** (Project → Manage → General)

### 2. Add credentials to app.py
Open `app.py` and replace:
```
IBM_API_KEY    = "YOUR_IBM_API_KEY"
IBM_PROJECT_ID = "YOUR_PROJECT_ID"
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run
```bash
python app.py
```

Open http://localhost:8080 in your browser.

---

## Deploy to IBM Code Engine

1. Push this folder to GitHub
2. Go to cloud.ibm.com → Code Engine → Create Application
3. Choose "Source code" → paste your GitHub repo URL
4. Set port to 8080 → Deploy

---

## Project Structure
```
research-agent/
├── app.py              ← Flask backend + IBM Granite API
├── requirements.txt    ← Python dependencies
├── Dockerfile          ← For IBM Code Engine deployment
└── templates/
    └── index.html      ← Frontend UI
```
