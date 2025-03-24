class User:
    def __init__(self, username):
        self.username = username.lower()

class Listing:
    def __init__(self, listing_id, title, description, price, category, username, created_at):
        self.id = listing_id
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.username = username
        self.created_at = created_at