from database import get_db_connection
from models import User, Listing

class Marketplace:
    @staticmethod
    def register_user(username):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT username FROM users WHERE LOWER(username) = LOWER(?)", (username,))
        if cur.fetchone():
            return "Error - user already existing"
        cur.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        return "Success"

    @staticmethod
    def create_listing(username, title, description, price, category):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT username FROM users WHERE LOWER(username) = LOWER(?)", (username,))
        if not cur.fetchone():
            return "Error - unknown user"
        cur.execute("INSERT INTO listings (title, description, price, category, username) VALUES (?, ?, ?, ?, ?)",
                    (title, description, price, category, username))
        listing_id = cur.lastrowid + 100000
        conn.commit()
        return str(listing_id)

    @staticmethod
    def delete_listing(username, listing_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT username FROM listings WHERE id = ?", (listing_id - 100000,))
        owner = cur.fetchone()
        if not owner:
            return "Error - listing does not exist"
        if owner[0].lower() != username.lower():
            return "Error - listing owner mismatch"
        cur.execute("DELETE FROM listings WHERE id = ?", (listing_id - 100000,))
        conn.commit()
        return "Success"

    @staticmethod
    def get_listing(username, listing_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT title, description, price, created_at, category, username FROM listings WHERE id = ?",
                    (listing_id - 100000,))
        listing = cur.fetchone()
        if not listing:
            return "Error - not found"
        return "|".join(map(str, listing))

    @staticmethod
    def get_category(username, category):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT title, description, price, created_at FROM listings WHERE LOWER(category) = LOWER(?) ORDER BY created_at DESC",
                    (category,))
        listings = cur.fetchall()
        if not listings:
            return "Error - category not found"
        return "\n".join(["|".join(map(str, lst)) for lst in listings])

    @staticmethod
    def get_top_category(username):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM users WHERE LOWER(username) = LOWER(?)", (username,))
        if not cur.fetchone():
            return "Error - unknown user"
        
        cur.execute("SELECT category, COUNT(*) FROM listings GROUP BY category")
        category_counts = cur.fetchall()
        if not category_counts:
            return ""

        max_count = max([count for _, count in category_counts])
        top_categories = sorted([cat for cat, count in category_counts if count == max_count])
        return " ".join(top_categories)