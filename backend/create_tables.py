from backend.database import (
    Base,
    engine
)

from backend.models.chat import Chat
from backend.models.chat_history import ChatHistory

Base.metadata.create_all(
    bind=engine
)

print("Database Tables Created")