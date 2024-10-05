# Persistence Layer
class DatabaseAccess:
    def __init__(self):
        self.data = {
            "users": [],
            "places": [],
            "reviews": [],
            "amenities": []
        }

    def save_user(self, user):
        self.data["users"].append(user)

    def save_place(self, place):
        self.data["places"].append(place)

    def save_review(self, review):
        self.data["reviews"].append(review)

    def save_amenity(self, amenity):
        self.data["amenities"].append(amenity)

    def get_users(self):
        return self.data["users"]

    def get_places(self):
        return self.data["places"]

    def get_reviews(self):
        return self.data["reviews"]

    def get_amenities(self):
        return self.data["amenities"]


# Business Logic Layer
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Place:
    def __init__(self, place_id, title, description):
        self.place_id = place_id
        self.title = title
        self.description = description


class Review:
    def __init__(self, review_id, user, place, rating, comment):
        self.review_id = review_id
        self.user = user
        self.place = place
        self.rating = rating
        self.comment = comment


class Amenity:
    def __init__(self, amenity_id, name, description):
        self.amenity_id = amenity_id
        self.name = name
        self.description = description


# Facade Layer
class HBnBFacade:
    def __init__(self):
        self.database = DatabaseAccess()

    def register_user(self, user_id, name):
        user = User(user_id, name)
        self.database.save_user(user)

    def create_place(self, place_id, title, description):
        place = Place(place_id, title, description)
        self.database.save_place(place)

    def submit_review(self, review_id, user, place, rating, comment):
        review = Review(review_id, user, place, rating, comment)
        self.database.save_review(review)

    def add_amenity(self, amenity_id, name, description):
        amenity = Amenity(amenity_id, name, description)
        self.database.save_amenity(amenity)

    def get_all_users(self):
        return self.database.get_users()

    def get_all_places(self):
        return self.database.get_places()

    def get_all_reviews(self):
        return self.database.get_reviews()

    def get_all_amenities(self):
        return self.database.get_amenities()


# Example Usage
if __name__ == "__main__":
    facade = HBnBFacade()

    # Register a user
    facade.register_user(1, "John Doe")

    # Create a place
    facade.create_place(101, "Beach House", "A beautiful beach house.")

    # Submit a review
    user = facade.get_all_users()[0]
    place = facade.get_all_places()[0]
    facade.submit_review(1001, user, place, 5, "Amazing place!")

    # Add an amenity
    facade.add_amenity(201, "WiFi", "High-speed internet access.")

    # Retrieve and print data
    print("Users:", facade.get_all_users())
    print("Places:", facade.get_all_places())
    print("Reviews:", facade.get_all_reviews())
    print("Amenities:", facade.get_all_amenities())
