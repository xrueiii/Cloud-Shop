from app.persistence.userRepository import UserRepository
from app.persistence.listingRepository import ListingRepository

class MarketplaceService:
    @staticmethod
    def register_user(username):
        if UserRepository.exists(username):
            return "Error - user already existing"
        UserRepository.save(username)
        return "Success"

    @staticmethod
    def create_listing(username, title, description, price, category):
        if not UserRepository.exists(username):
            return "Error - unknown user"
        listing_id = ListingRepository.create(title, description, price, category, username)
        return str(listing_id)

    @staticmethod
    def delete_listing(username, listing_id):
        owner = ListingRepository.get_owner(listing_id)
        if not owner:
            return "Error - listing does not exist"
        if owner[0].lower() != username.lower():
            return "Error - listing owner mismatch"
        ListingRepository.delete(listing_id)
        return "Success"

    @staticmethod
    def get_listing(username, listing_id):
        listing = ListingRepository.find_by_id(listing_id)
        if not listing:
            return "Error - not found"
        return "|".join(map(str, listing))

    @staticmethod
    def get_category(username, category):
        listings = ListingRepository.find_by_category(category)
        if not listings:
            return "Error - category not found"
        return "\n".join(["|".join(map(str, lst)) for lst in listings])

    @staticmethod
    def get_top_category(username):
        if not UserRepository.exists(username):
            return "Error - unknown user"

        category_counts = ListingRepository.get_category_counts()
        if not category_counts:
            return ""

        max_count = max([count for _, count in category_counts])
        top_categories = sorted([cat for cat, count in category_counts if count == max_count])
        return " ".join(top_categories)
