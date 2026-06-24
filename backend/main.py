from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from backend.database import SessionLocal, engine

from backend.models.chat_history import ChatHistory

from backend.rag.retriever import retrieve

from backend.services.llm_service import generate_answer
from backend.services.memory_service import (
    save_message,
    get_history
)

from backend.services.verse_service import get_daily_verse
from backend.services.image_service import generate_image
from backend.services.prayer_service import generate_prayer


app = FastAPI(title="FaithGPT")


# =====================================
# CREATE TABLES
# =====================================

ChatHistory.metadata.create_all(bind=engine)


# =====================================
# STATIC FILES
# =====================================

app.mount(
    "/generated_images",
    StaticFiles(directory="generated_images"),
    name="generated_images"
)


# =====================================
# CORS
# =====================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================
# REQUEST MODELS
# =====================================

class ChatRequest(BaseModel):
    user_id: int
    question: str


class ImageRequest(BaseModel):
    prompt: str


class PrayerRequest(BaseModel):
    problem: str


# =====================================
# ROOT
# =====================================

@app.get("/")
def root():

    return {
        "message": "FaithGPT Running Successfully"
    }


# =====================================
# CHAT
# =====================================

@app.post("/chat")
def chat(request: ChatRequest):

    db = SessionLocal()

    try:

        save_message(
            db,
            request.user_id,
            "user",
            request.question
        )

        question_lower = (
            request.question.lower()
        )

        personal_questions = [

            "what is my name",

            "who am i",

            "what am i learning",

            "what am learning",

            "remember me",

            "about me",

            "my name",

            "my learning",

            "what do you know about me"
        ]

        is_personal_question = any(
            keyword in question_lower
            for keyword in personal_questions
        )

        context = ""

        citations = []

        memory_text = ""

        # MEMORY QUESTIONS

        if is_personal_question:

            memory_messages = get_history(
                db,
                request.user_id
            )

            for msg in memory_messages:

                memory_text += (
                    f"{msg.role}: "
                    f"{msg.content}\n"
                )

        # BIBLE QUESTIONS

        else:

            docs = retrieve(
                request.question
            )

            for doc in docs:

                reference = doc.metadata.get(
                    "reference",
                    "Unknown Reference"
                )

                context += f"""
Reference:
{reference}

Verse:
{doc.page_content}

---------------------
"""

                citations.append(
                    reference
                )

        answer = generate_answer(
            request.question,
            context,
            memory_text
        )

        save_message(
            db,
            request.user_id,
            "assistant",
            answer
        )

        chat_entry = ChatHistory(
            user_id=request.user_id,
            question=request.question,
            answer=answer
        )

        db.add(chat_entry)

        db.commit()

        return {
            "answer": answer,
            "citations": (
                citations
                if not is_personal_question
                else []
            )
        }

    finally:

        db.close()


# =====================================
# MEMORY
# =====================================

@app.get("/memory/{user_id}")
def memory(user_id: int):

    db = SessionLocal()

    try:

        messages = get_history(
            db,
            user_id
        )

        return [

            {
                "role": m.role,
                "content": m.content
            }

            for m in messages

        ]

    finally:

        db.close()


# =====================================
# CHAT HISTORY
# =====================================

@app.get("/history/{user_id}")
def history(user_id: int):

    db = SessionLocal()

    try:

        chats = (

            db.query(ChatHistory)

            .filter(
                ChatHistory.user_id == user_id
            )

            .order_by(
                ChatHistory.id.desc()
            )

            .all()

        )

        return [

            {
                "id": chat.id,
                "question": chat.question,
                "answer": chat.answer
            }

            for chat in chats

        ]

    finally:

        db.close()


# =====================================
# DELETE SINGLE CHAT
# =====================================

@app.delete("/history/{chat_id}")
def delete_chat(chat_id: int):

    db = SessionLocal()

    try:

        chat = (

            db.query(ChatHistory)

            .filter(
                ChatHistory.id == chat_id
            )

            .first()

        )

        if not chat:

            return {
                "success": False,
                "message": "Chat not found"
            }

        db.delete(chat)

        db.commit()

        return {
            "success": True
        }

    finally:

        db.close()


# =====================================
# DAILY VERSE
# =====================================

@app.get("/daily-verse")
def daily_verse():

    return get_daily_verse()


# =====================================
# IMAGE GENERATION
# =====================================

@app.post("/generate-image")
def image(request: ImageRequest):

    image_path = generate_image(
        request.prompt
    )

    if image_path is None:

        return {
            "error": "Image generation failed"
        }

    return {

        "image_path": image_path

    }


# =====================================
# PRAYER ASSISTANT
# =====================================

@app.post("/prayer")
def prayer(request: PrayerRequest):

    prayer_text = generate_prayer(
        request.problem
    )

    return {

        "prayer": prayer_text

    }