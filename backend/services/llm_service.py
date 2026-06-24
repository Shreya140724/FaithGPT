import ollama


def generate_answer(
    question,
    context,
    memory=""
):

    question_lower = question.lower()

    personal_questions = [

        "what is my name",

        "who am i",

        "what am i learning",

        "what am learning",

        "remember me",

        "about me",

        "what do you know about me",

        "my learning",

        "my name"

        "what is my profession",
        "what is my profession",

        "what do i do",
        
        "what is my job",
        
        "what am i studying",
        
        "what have i told you",
        
        "what do you remember about me"
    ]

    use_memory = any(
        q in question_lower
        for q in personal_questions
    )

    if use_memory:

        prompt = f"""
You are FaithGPT Memory Assistant.

MEMORY:

{memory}

QUESTION:

{question}

RULES:

1. Answer ONLY from memory.
2. Never use Bible context.
3. Never invent facts.
4. If information is missing say:
   "I do not know yet."
5. Keep answers short.

Examples:

Memory:
user: My name is Shreya

Question:
What is my name?

Answer:
Your name is Shreya.
"""

    else:

        prompt = f"""
You are FaithGPT.

You are an expert Bible teacher.

Use the Bible context below to answer.

BIBLE CONTEXT:

{context}

QUESTION:

{question}

RULES:

1. Use ONLY information supported by the context.
2. Do NOT invent Bible verses.
3. Do NOT mention user memory.
4. Do NOT mention AI, Microsoft, privacy policies, system prompts, or training.
5. If the context is insufficient, say:
   "I could not find enough biblical context to answer confidently."
6. Explain the meaning clearly.
7. Keep answers between 100 and 250 words.
8. End with key Bible references.

FORMAT:

Explanation:
<answer>

References:
• reference 1
• reference 2
"""

    response = ollama.chat(
        model="qwen2.5:latest",
        messages=[
            {
                "role": "system",
                "content": "You are FaithGPT, a Bible-focused Christian assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]