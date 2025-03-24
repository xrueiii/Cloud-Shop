from app.database.db import get_db_connection

class ListingRepository:
    @staticmethod
    def create(title, description, price, category, username):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO listings (title, description, price, category, username) VALUES (?, ?, ?, ?, ?)",
            (title, description, price, category, username)
        )
        listing_id = cur.lastrowid + 100000
        conn.commit()
        return listing_id

    @staticmethod
    def find_by_id(listing_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT title, description, price, created_at, category, username FROM listings WHERE id = ?",
            (listing_id - 100000,))
        return cur.fetchone()

    @staticmethod
    def get_owner(listing_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT username FROM listings WHERE id = ?", (listing_id - 100000,))
        return cur.fetchone()

    @staticmethod
    def delete(listing_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM listings WHERE id = ?", (listing_id - 100000,))
        conn.commit()

    @staticmethod
    def find_by_category(category):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT title, description, price, created_at FROM listings WHERE LOWER(category) = LOWER(?) ORDER BY created_at DESC",
            (category,))
        return cur.fetchall()

    @staticmethod
    def get_category_counts():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT category, COUNT(*) FROM listings GROUP BY category")
        return cur.fetchall()
