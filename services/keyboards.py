from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍿 Что посмотреть")],
        [
            KeyboardButton(text="😂 Комедия"),
            KeyboardButton(text="😱 Ужасы"),
        ],
        [
            KeyboardButton(text="🚀 Фантастика"),
            KeyboardButton(text="🔥 Боевик"),
        ],
        [
            KeyboardButton(text="❤️ Для свидания"),
            KeyboardButton(text="👨‍👩‍👧 Семейный"),
        ],
        [
            KeyboardButton(text="🎲 Случайный фильм"),
            KeyboardButton(text="⭐ ТОП фильмов"),
        ],
        [
            KeyboardButton(text="🔎 Поиск фильма"),
        ],
    ],
    resize_keyboard=True,
)
