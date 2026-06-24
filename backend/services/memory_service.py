from sqlalchemy.orm import Session
from backend.models.chat import Chat


def save_message(

        db: Session,

        user_id,

        role,

        content):

    chat = Chat(

        user_id=user_id,

        role=role,

        content=content
    )

    db.add(chat)

    db.commit()


def get_history(

        db: Session,

        user_id):

    return (

        db.query(Chat)

        .filter(
            Chat.user_id ==
            user_id
        )

        .order_by(
            Chat.id.desc()
        )

        .limit(20)

        .all()
    )