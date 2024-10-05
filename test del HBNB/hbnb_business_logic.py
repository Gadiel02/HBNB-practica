import uuid
from datetime import datetime

# Capa de Lógica de Negocio

class User:
    def __init__(self, first_name, last_name, email, password):
        self.user_id = str(uuid.uuid4())  # ID único
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = False
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_profile(self, first_name=None, last_name=None, email=None, password=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if password:
            self.password = password
        self.updated_at = datetime.now()

class Place:
    def __init__(self, title, description, price, latitude, longitude):
        self.place_id = str(uuid.uuid4())  # ID único
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = []
        self.owner = None  # Referencia al propietario (User)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def set_owner(self, user):
        self.owner = user

class Review:
    def __init__(self, rating, comment, place, user):
        self.review_id = str(uuid.uuid4())  # ID único
        self.rating = rating
        self.comment = comment
        self.place = place  # Referencia a Place
        self.user = user    # Referencia a User
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class Amenity:
    def __init__(self, name, description):
        self.amenity_id = str(uuid.uuid4())  # ID único
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un usuario
    user = User("John", "Doe", "john.doe@example.com", "password123")

    # Crear un lugar
    place = Place("Cozy Cottage", "A cozy cottage in the woods", 100, 34.0522, -118.2437)
    place.set_owner(user)

    # Crear un amenity
    amenity = Amenity("Wifi", "High-speed internet access")
    place.add_amenity(amenity)

    # Crear una reseña
    review = Review(5, "Fantastic stay!", place, user)

    # Imprimir detalles
    print(f"User: {user.first_name} {user.last_name}, Email: {user.email}")
    print(f"Place: {place.title}, Description: {place.description}, Owner: {place.owner.first_name}")
    print(f"Amenity: {place.amenities[0].name}, Review: {review.comment}, Rating: {review.rating}")
