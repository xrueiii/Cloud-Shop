from app.database.db import get_db_connection

class UserRepository:
    @staticmethod
    def exists(username: str) -> bool:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM users WHERE LOWER(username) = LOWER(?)", (username,))
        return cur.fetchone() is not None

    @staticmethod
    def save(username: str):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
