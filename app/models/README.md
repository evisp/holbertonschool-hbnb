# Models

This folder contains the core data models for the HBnB Evolution project. Each model represents a distinct entity within the application, encapsulating the data and behaviors relevant to that entity.

## BaseModel

**Objective:**  
The [`BaseModel`](https://github.com/evisp/holbertonschool-hbnb/blob/main/app/models/base_model.py) serves as the foundational class for all other models in the project. It provides common attributes and methods that are shared across all entities.

**Key Characteristics and Functionalities:**
- **ID:** A unique identifier (UUID) for each instance.
- **Timestamps:** Automatically manages `created_at` and `updated_at` timestamps.
- **Save Method:** Updates the `updated_at` timestamp whenever the object is modified.
- **Dictionary Representation:** Converts the model to a dictionary format, making it easy to serialize and transfer data.

## User

**Objective:**  
The [`User`](https://github.com/evisp/holbertonschool-hbnb/blob/main/app/models/user.py) model manages user-related data and actions within the application, such as registration, profile updates, and validation.

**Key Characteristics and Functionalities:**
- **Attributes:** `first_name`, `last_name`, `email`, `password`, `is_admin`.
- **Email Validation:** Ensures that the email follows a valid format.
- **Profile Management:** Allows updating of user profile details.
- **Dictionary Representation:** Excludes sensitive information like the password while converting to a dictionary.

## Place

**Objective:**  
The [`Place`](https://github.com/evisp/holbertonschool-hbnb/blob/main/app/models/place.py) model represents a property or listing within the application, including its details and associated amenities and reviews.

**Key Characteristics and Functionalities:**
- **Attributes:** `title`, `description`, `price`, `latitude`, `longitude`, `owner_id`.
- **Price Validation:** Ensures that the price is a non-negative value.
- **Geographical Validation:** Validates latitude and longitude within acceptable ranges.
- **Amenities Management:** Allows adding and managing amenities associated with a place.
- **Review Management:** Supports adding and removing reviews associated with a place.
- **Dictionary Representation:** Includes amenities, reviews, and owner details.

## Amenity

**Objective:**  
The [`Amenity`](https://github.com/evisp/holbertonschool-hbnb/blob/main/app/models/amenity.py) model represents a feature or service available at a `Place`, such as Wi-Fi or parking.

**Key Characteristics and Functionalities:**
- **Attributes:** `name`, `description`.
- **Update Method:** Allows updating of amenity details.
- **Dictionary Representation:** Includes name and description.

## Review

**Objective:**  
The [`Review`](https://github.com/evisp/holbertonschool-hbnb/blob/main/app/models/review.py) model handles user feedback and ratings for places within the application.

**Key Characteristics and Functionalities:**
- **Attributes:** `text`, `rating`, `place_id`, `user_id`.
- **Rating Validation:** Ensures the rating is between 1 and 5.
- **Dictionary Representation:** Includes the review text, rating, and associated place and user IDs.

---

This README gives an overview of each model's purpose and functionality, making it clear how they fit into the overall architecture of the HBnB Evolution project.