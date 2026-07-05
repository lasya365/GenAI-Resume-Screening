# GenAI-Resume-Screening
# 🤖 InterviewGPT – AI Resume Screening & Interview Coach

## 📌 Overview
InterviewGPT is an AI-powered application that analyzes resumes, extracts skills, generates interview questions using RAG, and evaluates candidate answers using Groq LLM.

It helps simulate real interview scenarios and provides structured feedback like a technical interviewer.

---

## 🚀 Features

- 📄 Upload Resume (PDF) and extract text
- 🧠 Automatic skill detection from resume
- 📚 Upload interview question PDFs
- 🔍 RAG-based interview question generation (ChromaDB)
- 🤖 AI-powered answer evaluation using Groq LLM
- 📊 Detailed feedback:
  - Technical Score
  - Communication Score
  - Strengths & Weaknesses
  - Missing concepts
  - Improved answer
  - Final recommendation
- 🌐 Streamlit UI

---

## 🏗️ Project Structure


app.py
evaluator.py
rag.py
resume_parser.py
skill_extractor.py
.env
.gitignore


---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/your-username/InterviewGPT.git
cd InterviewGPT


---

### 2. Create virtual environment (optional)

python -m venv venv
venv\Scripts\activate # Windows


---

### 3. Install dependencies

pip install -r requirements.txt


---

### 4. Add environment variables

Create a `.env` file:


GROQ_API_KEY=your_api_key_here


---

## ▶️ Run the application


streamlit run app.py


---

## 🧠 How it works

1. Upload resume PDF
2. Extract text using pdfplumber
3. Detect skills automatically
4. Upload interview questions PDF
5. Convert document into embeddings using ChromaDB
6. Retrieve relevant interview questions using RAG
7. Generate question using LLM
8. Candidate submits answer
9. Groq LLM evaluates response and gives feedback

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq LLM (Llama 3.3)
- LangChain
- ChromaDB
- pdfplumber
- HuggingFace Embeddings

---

## 🔐 Security

- API keys stored in `.env`
- `.env` file ignored using `.gitignore`
- No sensitive data is pushed to GitHub

---

## 📌 Future Improvements

- Resume scoring system (ATS score)
- Multi-candidate comparison
- Real-time interview chat mode
- Deployment on Streamlit Cloud / AWS

---
