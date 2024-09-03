# API Documentation

## Users

### Namespace: `/users`

The `users` namespace handles operations related to user management. It provides endpoints to create, retrieve, and update user information.

### Models

#### User Model

The `User` model represents the data structure for user-related operations. It includes the following fields:

- **first_name** (string, required): The first name of the user.
- **last_name** (string, required): The last name of the user.
- **email** (string, required): The email address of the user.
- **password** (string, required): The password for the user account.
- **is_admin** (boolean, optional): Indicates whether the user has administrative privileges.

### Endpoints

#### `POST /users`

**Description**: Register a new user.

**Request Format**:
```json
{
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "string",
    "is_admin": boolean
}
```

**Responses**:
- **201 Created**: User successfully created.
  ```json
  {
      "id": "string",
      "message": "User created successfully"
  }
  ```
- **400 Bad Request**: Email already registered or invalid input data.
  ```json
  {
      "error": "string"
  }
  ```

**Notes**:
- The system checks for email uniqueness. If the email is already registered, a 400 error is returned.
- Input data must include `first_name`, `last_name`, `email`, and `password`.

#### `GET /users`

**Description**: Retrieve a list of all users.

**Responses**:
- **200 OK**: Returns a list of users.
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

**Notes**:
- The response includes a list of all users with their `id`, `first_name`, `last_name`, and `email`.

#### `GET /users/<user_id>`

**Description**: Retrieve user details by user ID.

**Request Parameters**:
- **user_id** (path parameter): The ID of the user to retrieve.

**Responses**:
- **200 OK**: Returns the user details.
  ```json
  {
      "id": "string",
      "created_at": "string",
      "updated_at": "string",
      "first_name": "string",
      "last_name": "string",
      "email": "string",
      "is_admin": boolean
  }
  ```
- **404 Not Found**: User not found.
  ```json
  {
      "error": "User not found"
  }
  ```

**Notes**:
- Returns the user’s details including `id`, `created_at`, `updated_at`, `first_name`, `last_name`, `email`, and `is_admin`.

#### `PUT /users/<user_id>`

**Description**: Update user information.

**Request Format**:
```json
{
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "string"
}
```

**Request Parameters**:
- **user_id** (path parameter): The ID of the user to update.

**Responses**:
- **200 OK**: User updated successfully.
  ```json
  {
      "message": "User updated successfully"
  }
  ```
- **404 Not Found**: User not found.
  ```json
  {
      "error": "User not found"
  }
  ```
- **400 Bad Request**: Invalid input data.
  ```json
  {
      "error": "Invalid input data"
  }
  ```

**Notes**:
- Only `first_name`, `last_name`, `email`, and `password` can be updated. If any of these fields are missing, they will not be updated.
- If the user does not exist, a 404 error is returned.
- If the input data is invalid, a 400 error is returned.