from backend.services.llm_service import generate_answer

def generate_prayer(user_problem):

    prompt = f"""
You are a compassionate Christian prayer assistant.

User Situation:
{user_problem}

Create:

1. A personal prayer (5-10 lines)
2. A short biblical encouragement
3. Two Bible references
4. End with Amen.

Format:

🙏 Prayer

[Prayer]

📖 Encouragement

[Encouragement]

📚 References

- Reference 1
- Reference 2

Amen.
"""

    return generate_answer(
        prompt,
        "",
        ""
    )