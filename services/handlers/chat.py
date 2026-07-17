from aiogram import Router
from aiogram.types import Message

from services.openai_service import ask_ai

router = Router()


@router.message()
async def chat(message: Message):
    try:
        answer = ask_ai(message.text)
        await message.answer(answer)
    except Exception:
        await message.answer(
            "😔 Не удалось получить ответ от ИИ. Попробуйте немного позже."
        )
