# HBNB

## Business Logic  (Models)

### User Model

The `User` model represents a user in the HBnB system. Each user has attributes for personal details and administrative status.

#### Attributes
- `first_name` (str): The user's first name.
- `last_name` (str): The user's last name.
- `email` (str): The user's email address.
- `password` (str): The user's password.
- `is_admin` (bool, default=False): Indicates whether the user is an administrator.

#### Methods
- `validate_email()`: Validates the format of the email address using regex.
- `register()`: Simulates user registration. This method currently validates the email format and can be expanded with additional registration logic.
- `update_profile(first_name=None, last_name=None, email=None, password=None)`: Updates the user's profile information. It allows updating the first name, last name, email, and password.
- `delete()`: Simulates user deletion. This method is a placeholder for future deletion logic.

#### Example Usage
```python
user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="password123")
user.validate_email()
user.register()
user.update_profile(email="new.email@example.com")
user.delete()
```

### Place Model

The `Place` model represents a property listed on the HBnB platform. Each place has attributes that describe its details and functionality to manage amenities and reviews.

### Attributes
- `title` (str): The title of the place.
- `description` (str): A detailed description of the place.
- `price` (float): The price per night for booking the place.
- `latitude` (float): The latitude coordinate of the place's location.
- `longitude` (float): The longitude coordinate of the place's location.
- `owner_id` (str): The unique identifier of the user who owns the place.
- `amenities` (list): A list that stores amenities associated with the place.
- `reviews` (list): A list that stores reviews associated with the place.

#### Methods

##### `add_amenity(amenity)`
Adds an amenity to the place if it is not already included in the amenities list.

**Parameters:**
- `amenity`: The amenity to be added.

##### `add_review(review)`
Adds a review to the place if the review is an instance of the `Review` class.

**Parameters:**
- `review`: An instance of the `Review` class to be added.

##### `remove_review(review)`
Removes a review from the place if it exists in the reviews list.

**Parameters:**
- `review`: An instance of the `Review` class to be removed.

##### `to_dict()`
Converts the place object to a dictionary representation, including the list of amenities.

**Returns:**
- `dict`: A dictionary with place attributes and amenities.

#### Example Usage

```python
from app.models.place import Place
from app.models.review import Review

# Create a Place object
place = Place(
    title="Cozy Apartment",
    description="A nice place to stay",
    price=100,
    latitude=37.7749,
    longitude=-122.4194,
    owner_id="user_id"
)

# Add an amenity
place.add_amenity("Wi-Fi")

# Create a Review object
review = Review(text="Great stay!", rating=5, place_id="place_id", user_id="user_id")

# Add a review to the place
place.add_review(review)

# Remove a review from the place
place.remove_review(review)

# Convert the Place object to a dictionary
place_dict = place.to_dict()
```

### Review Model

The `Review` model represents a review left by a user for a place on the HBnB platform. Each review contains details about the user's experience and rating.

#### Attributes
- `text` (str): The content of the review left by the user.
- `rating` (int): The rating given by the user, typically on a scale (e.g., 1 to 5).
- `place_id` (str): The unique identifier of the place being reviewed.
- `user_id` (str): The unique identifier of the user who left the review.

#### Methods

##### `to_dict()`
Converts the review object to a dictionary representation.

**Returns:**
- `dict`: A dictionary with review attributes.

##### Example Usage

```python
from app.models.review import Review

# Create a Review object
review = Review(
    text="Great stay!",
    rating=5,
    place_id="place_id",
    user_id="user_id"
)

# Convert the Review object to a dictionary
review_dict = review.to_dict()
```

### Amenity

The `Amenity` model represents an amenity that can be associated with a place on the HBnB platform. Amenities are features or services provided by a place that can enhance the user's experience.

#### Attributes
- `name` (str): The name of the amenity (e.g., "Pool", "WiFi").
- `description` (str): A description of the amenity, detailing what it offers.

#### Methods

##### `to_dict()`
Converts the amenity object to a dictionary representation.

**Returns:**
- `dict`: A dictionary with amenity attributes.

#### Example Usage

```python
from app.models.amenity import Amenity

# Create an Amenity object
amenity = Amenity(
    name="Swimming Pool",
    description="A large outdoor swimming pool."
)

# Convert the Amenity object to a dictionary
amenity_dict = amenity.to_dict()
```

