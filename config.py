import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не найден в .env")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY не найден в .env")
