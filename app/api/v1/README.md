# API Endpoints

This documentation provides an overview of the RESTful API endpoints for the HBnB Evolution project. These endpoints allow clients to interact with the application's core entities: **Users**, **Amenities**, **Places**, and **Reviews**. Each section outlines the available operations and the expected inputs and outputs.

## Overview
- **Base URL:** `/api/v1/`
- **Content-Type:** `application/json`
- **Authorization:** No authorization is required for these endpoints.

## Users API
The Users API manages operations related to user entities, including user registration, retrieval, and updating user profiles.

### **Endpoint:** `/users/`
- **POST**: Register a new user.
  - **Request Body**:
    ```json
    {
      "first_name": "string",
      "last_name": "string",
      "email": "string",
      "password": "string",
      "is_admin": "boolean"  # Optional
    }
    ```
  - **Responses**:
    - `201`: User successfully created.
    - `400`: Email already registered or invalid input data.

- **GET**: Retrieve all users.
  - **Responses**:
    - `200`: Successfully retrieved a list of users.
    - **Response Example**:
      ```json
      [
        {
          "id": "string",
          "first_name": "string",
          "last_name": "string",
          "email": "string"
        }
      ]
      ```

### **Endpoint:** `/users/<user_id>`
- **GET**: Retrieve user details by ID.
  - **Responses**:
    - `200`: Successfully retrieved user details.
    - `404`: User not found.

- **PUT**: Update user information.
  - **Request Body**:
    ```json
    {
      "first_name": "string",
      "last_name": "string",
      "email": "string",
      "password": "string"  # Optional
    }
    ```
  - **Responses**:
    - `200`: User successfully updated.
    - `404`: User not found.
    - `400`: Invalid input data.

## Amenities API
The Amenities API manages operations related to amenity entities, including adding new amenities and retrieving or updating existing amenities.

### **Endpoint:** `/amenities/`
- **POST**: Register a new amenity.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "description": "string"  # Optional
    }
    ```
  - **Responses**:
    - `201`: Amenity successfully created.
    - `400`: Invalid input data.

- **GET**: Retrieve all amenities.
  - **Responses**:
    - `200`: Successfully retrieved a list of amenities.
    - **Response Example**:
      ```json
      [
        {
          "id": "string",
          "name": "string",
          "description": "string"
        }
      ]
      ```

### **Endpoint:** `/amenities/<amenity_id>`
- **GET**: Retrieve amenity details by ID.
  - **Responses**:
    - `200`: Successfully retrieved amenity details.
    - `404`: Amenity not found.

- **PUT**: Update an amenity's information.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "description": "string"  # Optional
    }
    ```
  - **Responses**:
    - `200`: Amenity successfully updated.
    - `404`: Amenity not found.
    - `400`: Invalid input data.

## Places API
The Places API manages operations related to place entities, including registering new places and retrieving or updating existing places.

### **Endpoint:** `/places/`
- **POST**: Register a new place.
  - **Request Body**:
    ```json
    {
      "title": "string",
      "description": "string",
      "price": "float",
      "latitude": "float",
      "longitude": "float",
      "owner_id": "string"
    }
    ```
  - **Responses**:
    - `201`: Place successfully created.
    - `400`: Owner not found or invalid input data.

- **GET**: Retrieve all places.
  - **Responses**:
    - `200`: Successfully retrieved a list of places.
    - **Response Example**:
      ```json
      [
        {
          "id": "string",
          "title": "string",
          "latitude": "float",
          "longitude": "float"
        }
      ]
      ```

### **Endpoint:** `/places/<place_id>`
- **GET**: Retrieve place details by ID.
  - **Responses**:
    - `200`: Successfully retrieved place details, including owner, amenities, and reviews.
    - `404`: Place not found.

- **PUT**: Update a place's information.
  - **Request Body**:
    ```json
    {
      "title": "string",
      "description": "string",
      "price": "float",
      "latitude": "float",
      "longitude": "float"
    }
    ```
  - **Responses**:
    - `200`: Place successfully updated.
    - `404`: Place not found.
    - `400`: Invalid input data.

## Reviews API
The Reviews API manages operations related to review entities, including creating, retrieving, updating, or deleting reviews associated with places.

### **Endpoint:** `/reviews/`
- **POST**: Create a new review.
  - **Request Body**:
    ```json
    {
      "text": "string",
      "rating": "integer",
      "place_id": "string",
      "user_id": "string"
    }
    ```
  - **Responses**:
    - `201`: Review successfully created.
    - `400`: Invalid input data.

- **GET**: Retrieve all reviews.
  - **Responses**:
    - `200`: Successfully retrieved a list of reviews.
    - **Response Example**:
      ```json
      [
        {
          "id": "string",
          "text": "string",
          "rating": "integer",
          "place_id": "string",
          "user_id": "string"
        }
      ]
      ```

### **Endpoint:** `/reviews/<review_id>`
- **GET**: Retrieve review details by ID.
  - **Responses**:
    - `200`: Successfully retrieved review details.
    - `404`: Review not found.

- **PUT**: Update a review's information.
  - **Request Body**:
    ```json
    {
      "text": "string",
      "rating": "integer"
    }
    ```
  - **Responses**:
    - `200`: Review successfully updated.
    - `404`: Review not found.
    - `400`: Invalid input data.

- **DELETE**: Delete a review.
  - **Responses**:
    - `204`: Review successfully deleted.
    - `404`: Review not found.

