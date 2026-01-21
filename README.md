# Jarvis AI – Self-Hosted Enterprise Copilot

Jarvis AI is a self-hosted, retrieval-augmented AI assistant built to demonstrate how modern enterprise copilots are designed and implemented in real-world systems.

This project goes beyond simple LLM API calls and focuses on **architecture, data retrieval, debugging, and system integration**, closely mirroring how AI assistants are built in production environments.

---

## Why This Project

Most AI demos only showcase prompt → response flows.  
In real companies, AI systems must:

- Work with **private or internal data**
- Retrieve **relevant context before answering**
- Be **controllable and self-hosted**
- Handle **SDK breaking changes**
- Be structured, testable, and deployable

Jarvis AI was built with those constraints in mind.

---

## What Jarvis AI Does

- Runs a **self-hosted LLM** locally (LLaMA via Ollama)
- Stores custom knowledge in a **vector database (Pinecone)**
- Uses **Retrieval Augmented Generation (RAG)** to answer accurately
- Exposes a clean **FastAPI backend**
- Provides a simple **chat-based interface**
- Keeps secrets secure using environment variables

---

## Tech Stack

### Backend
- Python
- FastAPI
- LangChain (community integrations)
- SentenceTransformers (embeddings)

### LLM
- LLaMA (served locally using Ollama)

### Vector Database
- Pinecone (semantic search)

### Frontend
- Streamlit (chat UI)

---

## System Architecture

User
↓
Chat UI (Streamlit)
↓
FastAPI Backend
↓
Embedding Model
↓
Pinecone Vector Search
↓
Relevant Context
↓
Local LLM (LLaMA via Ollama)
↓
Final Answer


---

## Key Engineering Highlights

- Designed a **modular RAG pipeline** from scratch
- Migrated code to handle **LangChain and Pinecone SDK breaking changes**
- Clean separation of concerns (embeddings, retrieval, inference)
- Secure handling of secrets using `.env` and `.gitignore`
- Debugged real Windows + multiprocessing + dependency issues
- Built with extensibility in mind (LLM, DB, UI can be swapped)

---

## Project Structure

JARVIS/
│
├── backend/
│ ├── main.py # FastAPI entry point
│ ├── rag.py # Pinecone retrieval logic
│ ├── embeddings.py # Embedding model
│ └── init.py
│
├── frontend/
│ └── app.py # Streamlit chat UI
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Running the Project Locally

### Prerequisites
- Python 3.10+
- Ollama installed and running
- A Pinecone account

---

### Start the Backend

```bash
cd backend
uvicorn main:app --reload

Open the API docs:
http://127.0.0.1:8000/docs

Start the Frontend
cd frontend
streamlit run app.py

DEMO Link :- https://drive.google.com/file/d/1KVdnSg6C0EyQWgdIoiK1WgLLSa1ZFmV1/view?usp=sharing
