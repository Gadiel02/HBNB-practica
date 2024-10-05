# hbnb_sequence_diagrams.py

# Sequence Diagram for User Registration
user_registration = """
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: Register User
    API->>BusinessLogic: Validate Input
    BusinessLogic->>Database: Save User Data
    Database-->>BusinessLogic: Confirm Save
    BusinessLogic-->>API: Return Success
    API-->>User: Registration Successful
"""

# Sequence Diagram for Place Creation
place_creation = """
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: Create Place
    API->>BusinessLogic: Validate Place Data
    BusinessLogic->>Database: Save Place Data
    Database-->>BusinessLogic: Confirm Save
    BusinessLogic-->>API: Return Success
    API-->>User: Place Created
"""

# Sequence Diagram for Review Submission
review_submission = """
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: Submit Review
    API->>BusinessLogic: Validate Review Data
    BusinessLogic->>Database: Save Review Data
    Database-->>BusinessLogic: Confirm Save
    BusinessLogic-->>API: Return Success
    API-->>User: Review Submitted
"""

# Sequence Diagram for Fetching a List of Places
fetch_places = """
sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: Fetch Places
    API->>BusinessLogic: Request List of Places
    BusinessLogic->>Database: Retrieve Places
    Database-->>BusinessLogic: Return Places Data
    BusinessLogic-->>API: Send Places Data
    API-->>User: Return Places List
"""

# Output the diagrams to the console or a file
if __name__ == "__main__":
    with open("hbnb_sequence_diagrams.mmd", "w") as file:
        file.write(user_registration)
        file.write("\n\n")
        file.write(place_creation)
        file.write("\n\n")
        file.write(review_submission)
        file.write("\n\n")
        file.write(fetch_places)

    print("Sequence diagrams written to hbnb_sequence_diagrams.mmd")
