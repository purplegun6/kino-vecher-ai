from html import escape


def format_movie(movie):
    if movie is None:
        return "😔 Фильм не найден."

    title = escape(str(movie["title"] or "Без названия"))
    year = movie["year"] or "—"
    genre = escape(str(movie["genre"] or "Не указан"))
    country = escape(str(movie["country"] or "Не указана"))
    duration = movie["duration"] or "—"
    rating = movie["rating"] or "—"
    description = escape(str(movie["description"] or "Описание отсутствует."))

    text = f"""
🎬 <b>{title}</b>

⭐ <b>IMDb:</b> {rating}
📅 <b>Год:</b> {year}
🎭 <b>Жанр:</b> {genre}
🌍 <b>Страна:</b> {country}
⏱ <b>Длительность:</b> {duration} мин.

📝 <b>Описание:</b>

{description}
"""

    return text.strip()
