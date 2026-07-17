from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_ai(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты — дружелюбный эксперт по фильмам. "
                    "Помогай выбирать фильмы и отвечай кратко и понятно."
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        max_tokens=500,
    )

    return response.choices[0].message.content
