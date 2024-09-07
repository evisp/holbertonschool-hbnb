# HBnB Evolution

## Overview

HBnB Evolution is a simplified application inspired by AirBnB, designed to manage users, places, amenities, and reviews. The project is organized into multiple layers to ensure clean architecture, maintainability, and scalability. The main components include:

- **API**: Exposes the endpoints for interacting with the application.
- **Models**: Define the core data structures and business logic.
- **Persistence**: Handles data storage and retrieval.
- **Facade (Services)**: Acts as an intermediary between the API and the persistence layer, coordinating business logic.

![Class Diagram](../../figs/packagediagram.jpeg)


## How It All Connects

The application is structured to ensure that each component has a well-defined role:

1. **API**: Handles HTTP requests and routes them to the appropriate Facade methods.
2. **Facade**: Coordinates between API calls and the business logic encapsulated in models and persistence operations.
3. **Models**: Define the data structures and business rules that govern the application’s entities.
4. **Persistence**: Manages the data storage, ensuring that models are saved and retrieved as needed.

Each component is designed to be modular and can be updated or replaced without impacting the overall system, making the project scalable and maintainable.


## Key Components

### API

The API layer is built using Flask-RESTx, providing RESTful endpoints for each entity in the system (Users, Amenities, Places, Reviews). The endpoints handle CRUD operations, input validation, and error handling.

- **Endpoints**: Organized by entity (e.g., `/users`, `/places`, `/amenities`, `/reviews`).
- **Documentation**: Each endpoint is documented with expected input and output formats.

[See the API README for more details](./app/api/v1/README.md)

### Models

The Models layer defines the data structures representing the core entities in the system, such as User, Place, Amenity, and Review. Each model includes validation logic, methods for converting to and from dictionary representations, and integration with the persistence layer.

- **Entities**: User, Place, Amenity, Review.
- **Inheritance**: Common properties and methods are encapsulated in a `BaseModel` class.

[See the Models README for more details](./app/models/README.md)

### Persistence

The Persistence layer abstracts the data storage mechanism. Initially, an in-memory repository was used, but this can be replaced with a database-backed solution. This layer provides CRUD operations and query methods that are used by the Facade.

- **Repository Pattern**: Abstracts data access.
- **InMemoryRepository**: The initial implementation for development purposes.

[See the Persistence README for more details](./app/persistence/README.md)

### Facade (Services)

The Facade layer, also known as Services, acts as the intermediary between the API and the Persistence layer. It encapsulates the business logic and ensures that operations are performed consistently and correctly.

- **HBnBFacade**: The central class coordinating interactions between models, repositories, and API.
- **Patterns**: Implements a Facade pattern to simplify API interaction with the underlying layers.

[See the Services README for more details](./app/services/README.md)

## Configurations and Dependencies

### Config
The [config file](./config.py) contains environment-specific settings, such as secret keys and debug flags. It supports different configurations for development and production environments.

- **Config Class**: Manages application configuration settings.
- **DevelopmentConfig**: Extends the base config with development-specific settings.

### Requirements File

The [requirements](./requirements.txt) file lists all the dependencies needed to run the HBnB Evolution project. It includes Flask, Flask-RESTx, and pytest for testing.

- **Installation**: Use `pip install -r requirements.txt` to install dependencies.

### Run File

The [run](./run.py) file is used to start the Flask application. It initializes the application and runs it with the specified configuration settings.

- **Usage**: Run the application using `python run.py`.
