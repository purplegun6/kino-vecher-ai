import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "movies.db"


class SearchEngine:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row

    def random_movie(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT *
            FROM movies
            WHERE
                year >= 1990
                AND rating >= 7.0
                AND duration >= 70
            ORDER BY RANDOM()
            LIMIT 1
        """)

        return cursor.fetchone()

    def search_title(self, query, limit=10):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT *
            FROM movies
            WHERE
                title LIKE ?
                AND year >= 1990
            ORDER BY rating DESC
            LIMIT ?
        """, (f"%{query}%", limit))

        return cursor.fetchall()

    def search_genre(self, genre, limit=10):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT *
            FROM movies
            WHERE
                genre LIKE ?
                AND year >= 1990
                AND rating >= 7.0
                AND duration >= 70
            ORDER BY rating DESC
            LIMIT ?
        """, (f"%{genre}%", limit))

        return cursor.fetchall()

    def top_movies(self, limit=20):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT *
            FROM movies
            WHERE
                year >= 1990
                AND rating >= 7.5
                AND duration >= 70
            ORDER BY rating DESC
            LIMIT ?
        """, (limit,))

        return cursor.fetchall()

    def close(self):
        self.conn.close()
