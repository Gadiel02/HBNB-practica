# hbnb.py

# Capa de Persistencia
class Database:
    def __init__(self):
        self.data = {}

    def save(self, entity_id, entity):
        self.data[entity_id] = entity

    def get(self, entity_id):
        return self.data.get(entity_id, None)

# Capa de Lógica de Negocio
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
    def __init__(self, review_id, place_id, user_id, comment):
        self.review_id = review_id
        self.place_id = place_id
        self.user_id = user_id
        self.comment = comment

class Amenity:
    def __init__(self, amenity_id, name):
        self.amenity_id = amenity_id
        self.name = name

# Capa de Presentación (Facade)
class HBnB:
    def __init__(self):
        self.database = Database()

    def create_user(self, user_id, name):
        user = User(user_id, name)
        self.database.save(user_id, user)

    def create_place(self, place_id, title, description):
        place = Place(place_id, title, description)
        self.database.save(place_id, place)

    def create_review(self, review_id, place_id, user_id, comment):
        review = Review(review_id, place_id, user_id, comment)
        self.database.save(review_id, review)

    def get_user(self, user_id):
        return self.database.get(user_id)

    def get_place(self, place_id):
        return self.database.get(place_id)

    def get_review(self, review_id):
        return self.database.get(review_id)

# Ejemplo de uso
if __name__ == "__main__":
    hbnb = HBnB()
    hbnb.create_user("1", "Alice")
    hbnb.create_place("101", "Beautiful Apartment", "A lovely place to stay.")
    hbnb.create_review("1001", "101", "1", "Amazing experience!")

    user = hbnb.get_user("1")
    print(f"User: {user.name}")  # Output: User: Alice
    place = hbnb.get_place("101")
    print(f"Place: {place.title} - {place.description}")  # Output: Place: Beautiful Apartment - A lovely place to stay.
