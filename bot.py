import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🎬 <b>Добро пожаловать в КиноВечер AI!</b>\n\n"
        "Я помогу подобрать фильм на любой вкус.\n\n"
        "Напишите мне, например:\n"
        "• Хочу комедию\n"
        "• Посоветуй триллер\n"
        "• Что посмотреть вечером?"
    )


async def main():
    print("🤖 Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
