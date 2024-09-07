# Persistence Layer

The `persistence` layer in the HBnB Evolution project is responsible for managing data storage and retrieval. This layer abstracts the underlying storage mechanism, ensuring that the business logic can interact with data in a consistent manner, regardless of how or where it is stored.

## Key Components

### `Repository` (Abstract Base Class)
- **Objective**: Serves as the blueprint for all repository implementations in the project.
- **Key Characteristics**:
  - Defines the core CRUD operations (`add`, `get`, `get_all`, `update`, `delete`) and a method for querying by attributes (`get_by_attribute`).
  - Enforces a standard interface for any concrete repository, ensuring consistency across different storage implementations.

### `InMemoryRepository` (Concrete Implementation)
- **Objective**: Provides an in-memory storage solution, primarily useful for testing and development environments.
- **Key Characteristics**:
  - Implements the `Repository` interface, storing objects in a simple dictionary.
  - Supports adding, retrieving, updating, and deleting objects by their unique ID.
  - Allows querying objects based on their attributes.
  - Outputs debug information to the console for each operation, which can be useful during development.

## Future Extension
- **Database Respository**: This component will be added later to handle database-backed persistence, allowing the application to store data in a more permanent and scalable manner.

