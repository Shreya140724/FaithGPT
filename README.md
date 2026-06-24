# ✝️ FaithGPT

FaithGPT is an AI-powered Christian Assistant that combines Bible Question Answering, Memory-Based Conversations, Prayer Generation, Daily Bible Verses, and Christian Image Generation into a single modern web application.

Built using:

* FastAPI
* Next.js
* Ollama
* FAISS Vector Database
* HuggingFace Embeddings
* SQLite
* Tailwind CSS

---

## Features

### 📖 Bible Chat (RAG)

Ask questions about the Bible and receive answers grounded in Scripture.

Examples:

* Who was Joseph?
* Explain Romans 8:28
* What does the Bible teach about patience?
* Tell me about Moses

The system retrieves relevant Bible verses using FAISS semantic search and generates contextual answers using a local LLM through Ollama.

---

### 🧠 Personal Memory

FaithGPT remembers information shared by the user.

Examples:

* My name is Shreya
* I am an AI Engineer

Later you can ask:

* What is my name?
* What do you know about me?
* What am I learning?

Memory-based questions are answered from stored conversation history.

---

### 🙏 Prayer Assistant

Generate personalized Christian prayers.

Examples:

* Pray for my career
* Pray for my family
* Pray for anxiety and stress
* Pray for guidance

Each response includes:

* Personalized prayer
* Biblical encouragement
* Relevant Bible references

---

### 🖼 Christian Image Generation

Generate Christian-themed AI images from text prompts.

Examples:

* Jesus walking on water
* Moses parting the Red Sea
* Garden of Gethsemane
* Noah's Ark during sunset

Images are generated locally and displayed directly in the application.

---

### ✝ Daily Bible Verse

Displays a randomly selected Bible verse each time the application loads.

Examples:

* John 3:16
* Romans 8:28
* Philippians 4:13

---

### 🗑 Chat History Management

Features:

* New Chat
* Conversation History
* Delete Individual Chats
* Memory Storage

---

## Architecture

User Question

↓

Next.js Frontend

↓

FastAPI Backend

↓

FAISS Retriever

↓

Bible Context

↓

Ollama (Qwen 2.5)

↓

Generated Answer

---

## Tech Stack

### Frontend

* Next.js
* React
* Tailwind CSS
* Axios

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Ollama

### AI Components

* Qwen 2.5
* FAISS
* HuggingFace Embeddings
* RAG Pipeline

---

## Installation

### Clone Repository

git clone https://github.com/yourusername/FaithGPT.git

cd FaithGPT

### Backend

cd backend

pip install -r requirements.txt

uvicorn backend.main:app --reload

### Frontend

cd frontend

npm install

npm run dev

---

## Ollama Models

Install:

ollama pull qwen2.5

Start:

ollama serve

---

## Future Improvements

* Voice Assistant
* Bible Verse Search
* Multi-language Support
* User Authentication
* Conversation Export
* Bible Study Plans
* Christian Devotional Generator

---

## Screenshots

### Home Page

(Add screenshot)

### Bible Chat

(Add screenshot)

### Prayer Assistant

(Add screenshot)

### Image Generation

(Add screenshot)

### Memory Feature

(Add screenshot)

---

## Author

Shreya Sidabache

M.Tech Artificial Intelligence

AI Engineer | Computer Vision | Generative AI | RAG Systems
