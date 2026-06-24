from sqlalchemy import Column, Integer, Text
from backend.database import Base

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(Integer)

    question = Column(Text)

    answer = Column(Text)