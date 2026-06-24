from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class Chat(Base):

    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer)

    role = Column(String(50))

    content = Column(Text)