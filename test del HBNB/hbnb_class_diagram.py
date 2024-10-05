classDiagram
    class User {
        +user_id: String
        +first_name: String
        +last_name: String
        +email: String
        +created_at: DateTime
        +updated_at: DateTime
        +is_admin: Boolean
        +update_profile()
        +set_admin()
    }

    class Place {
        +place_id: String
        +title: String
        +description: String
        +price: Float
        +latitude: Float
        +longitude: Float
        +created_at: DateTime
        +updated_at: DateTime
        +add_amenity()
        +set_owner()
    }

    class Review {
        +review_id: String
        +rating: Int
        +comment: String
        +created_at: DateTime
        +updated_at: DateTime
        +update_comment()
    }

    class Amenity {
        +amenity_id: String
        +name: String
        +description: String
        +created_at: DateTime
        +updated_at: DateTime
    }

    User "1" --> "0..*" Review : "writes"
    Place "1" --> "0..*" Review : "receives"
    Place "1" --> "0..*" Amenity : "has"
    User "1" --> "0..*" Place : "owns"
