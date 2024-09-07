# Services Layer

The `services` layer in the HBnB Evolution project acts as an intermediary between the business logic and the persistence layer. It encapsulates the logic required to interact with various repositories and models, providing a simplified and consistent interface for managing the core entities within the application.

## Key Components

### `HBnBFacade`
- **Objective**: Centralizes and manages operations for different entities such as `User`, `Amenity`, `Place`, and `Review`. It provides a single entry point for interacting with these entities, ensuring consistent operations across the application.
- **Key Characteristics**:
  - Utilizes shared repositories for each entity, ensuring that data is consistent and accessible throughout the application.
  - Provides methods for creating, retrieving, updating, and deleting entities, with specific logic tailored to the needs of each model.

## Entity-Specific Operations

### **User Operations**
- **create_user(user_data)**: Creates a new `User` entity and stores it in the repository.
- **get_user(user_id)**: Retrieves a `User` entity by its unique ID.
- **get_user_by_email(email)**: Fetches a `User` entity based on the email attribute.
- **get_all_users()**: Returns a list of all `User` entities.
- **update_user(user)**: Updates the details of an existing `User` entity in the repository.

### **Amenity Operations**
- **create_amenity(amenity_data)**: Creates a new `Amenity` entity and stores it in the repository.
- **get_amenity(amenity_id)**: Retrieves an `Amenity` entity by its unique ID.
- **get_all_amenities()**: Returns a list of all `Amenity` entities.
- **update_amenity(amenity_id, amenity_data)**: Updates an existing `Amenity` entity with new data.

### **Place Operations**
- **create_place(place_data)**: Creates a new `Place` entity, ensuring that the specified owner exists before adding it to the repository.
- **get_place(place_id)**: Retrieves a `Place` entity by its unique ID, including associated `Owner`, `Amenity`, and `Review` details.
- **get_all_places()**: Returns a list of all `Place` entities, including detailed information about their owners and amenities.
- **update_place(place_id, place_data)**: Updates an existing `Place` entity with new data.

### **Review Operations**
- **create_review(review_data)**: Creates a new `Review` entity, ensuring that both the associated `Place` and `User` exist before adding it to the repository. Also associates the review with the `Place`.
- **get_review(review_id)**: Retrieves a `Review` entity by its unique ID.
- **get_all_reviews()**: Returns a list of all `Review` entities.
- **update_review(review_id, \*\*kwargs)**: Updates an existing `Review` entity with new data, validating the rating if it is being modified.
- **delete_review(review_id)**: Deletes a `Review` entity by its unique ID, removing it from the repository.
- **get_reviews_for_place(place_id)**: Retrieves all `Review` entities associated with a specific `Place`.

