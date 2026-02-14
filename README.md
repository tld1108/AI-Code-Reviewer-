# AI-Code-Reviewer
A simple, user-friendly web application. An AI-based application that analyzes source code, detects potential bugs, and provides structured feedback to improve code quality and maintainability.

---

# Features
1. Automated Code Quality Review
2. Bug Detection & Risk Identification
3. Performance Improvement Suggestions
4. Clean Code Recommendations
5. Basic Security Analysis
6. Custom Styled Streamlit UI

---

# Tech Stack
1. Python
2. FastAPI (Backend API)
3. Streamlit (Frontend UI)
4. Groq / OpenAI API (i'm using Groq since its free)
5. Poppins + Carla Fonts

---

# Project Structure
```bash
AI-Code-Reviewer/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI
│ └── reviewer.py # AI
│
├── steam_app.py 
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation 

### 1. Clone the repository.
```bash
git clone https://github.com/your-username/CodeInsight-AI.git
cd CodeInsight-AI
```

### 2. Install dependencies.
```bash
pip install -r requirements.txt
```

---

# Environment Variable

### Create a .env file in the root directory
```bash
GROQ_API_KEY=your_api_key_here (I use this, you can get the API from the GROQ website)
```
or
```bash
OPENAI_API_KEY=your_api_key_here
```

---

# Running the Application

### Start Backend (FastAPI)
```bash
uvicorn app.main:app --reload
```
### Start Frontend (Streamlit)
```bash
streamlit run streamlit_app.py
```
### Then open
```bash
http://localhost:8501
```

---

# How It Works
1. User uploads or pastes source code.
2. Streamlit sends the code to the FastAPI backend.
3. The backend calls the AI model.
4. Structured review feedback is returned and displayed.

---

# Future Improvements (just maybe.....)
1. Dark Mode UI
2. Pull Request integration (GitHub API)
3. Multi-language code support
4. CI/CD deployment
5. Docker containerization



