from backend.models.chat import Chat

def get_chat_history(
    db,
    user_id
):

    return (

        db.query(Chat)

        .filter(
            Chat.user_id == user_id
        )

        .order_by(
            Chat.id.desc()
        )

        .all()

    )