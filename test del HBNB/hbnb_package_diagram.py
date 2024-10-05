import uuid
from datetime import datetime

# User Entity
class User:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.user_id = str(uuid.uuid4())  # Unique identifier
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = datetime.now()  # Creation date
        self.updated_at = datetime.now()  # Update date
        self.is_admin = False  # Default user role

    def update_profile(self, first_name: str = None, last_name: str = None, email: str = None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        self.updated_at = datetime.now()

    def set_admin(self):
        self.is_admin = True


# Place Entity
class Place:
    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float):
        self.place_id = str(uuid.uuid4())  # Unique identifier
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = []  # List of associated amenities
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.owner: User = None  # Owner of the place

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def set_owner(self, user: User):
        self.owner = user
        self.updated_at = datetime.now()


# Review Entity
class Review:
    def __init__(self, user: User, place: Place, rating: int, comment: str):
        self.review_id = str(uuid.uuid4())  # Unique identifier
        self.user = user
        self.place = place
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_comment(self, comment: str):
        self.comment = comment
        self.updated_at = datetime.now()


# Amenity Entity
class Amenity:
    def __init__(self, name: str, description: str):
        self.amenity_id = str(uuid.uuid4())  # Unique identifier
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


# Example Usage
if __name__ == "__main__":
    # Create a user
    user1 = User("John", "Doe", "john.doe@example.com")
    user1.set_admin()  # Set as admin

    # Create a place
    place1 = Place("Beach House", "A beautiful beach house.", 250.0, 34.0522, -118.2437)
    place1.set_owner(user1)  # Set owner of the place

    # Create an amenity
    amenity1 = Amenity("WiFi", "High-speed internet access.")
    place1.add_amenity(amenity1)  # Add amenity to the place

    # Create a review
    review1 = Review(user1, place1, 5, "Amazing stay!")

    # Output attributes for demonstration
    print(f"User: {user1.first_name} {user1.last_name}, Admin: {user1.is_admin}")
    print(f"Place: {place1.title}, Owner: {place1.owner.first_name}")
    print(f"Amenity: {place1.amenities[0].name}, Description: {place1.amenities[0].description}")
    print(f"Review by {review1.user.first_name}: {review1.comment} (Rating: {review1.rating})")
