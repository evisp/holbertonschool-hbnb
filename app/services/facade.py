from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    _shared_user_repo = InMemoryRepository()
    _shared_place_repo = InMemoryRepository()
    _shared_review_repo = InMemoryRepository()
    _shared_amenity_repo = InMemoryRepository()

    def __init__(self):
        self.user_repo = HBnBFacade._shared_user_repo
        self.place_repo = HBnBFacade._shared_place_repo
        self.review_repo = HBnBFacade._shared_review_repo
        self.amenity_repo = HBnBFacade._shared_amenity_repo


    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        print(f"User created with ID: {user.id}")  # Debug print
        return user

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if user:
            print(f"Found user with ID: {user.id}")  # Debug print
        else:
            print(f"User with ID {user_id} not found")  # Debug print
        return user

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user):
        self.user_repo.update(user.id, user.to_dict())

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        # Fetch the existing amenity
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        
        # Update the amenity's attributes
        amenity.update(name=amenity_data.get('name', amenity.name),
                       description=amenity_data.get('description', amenity.description))
        
        # Update the repository
        self.amenity_repo.update(amenity_id, amenity.to_dict())
        return amenity
    
    def create_place(self, place_data):
        owner_id = place_data['owner_id']
        owner = self.user_repo.get(owner_id)

        if not owner:
            raise ValueError("Owner does not exist")
        
        # Remove the 'owner' key if it exists
        place_data.pop('owner', None)

        place = Place(**place_data)
        self.place_repo.add(place)
        return place
    
    def get_place(self, place_id):
        # Retrieve the place object
        place = self.place_repo.get(place_id)
        if not place:
            return None

        # Ensure place is a Place object before converting to dict
        place_dict = place.to_dict() if not isinstance(place, dict) else place

        owner = self.user_repo.get(place_dict.get('owner_id'))

        # Include owner details in the returned dictionary
        if owner:
            place_dict['owner'] = {
                "id": owner.id,
                "first_name": owner.first_name,
                "last_name": owner.last_name,
                "email": owner.email
            }

        # Ensure 'amenities' key exists and is iterable
        amenities_ids = place_dict.get('amenities', [])
        place_dict['amenities'] = [self.amenity_repo.get(amenity_id).to_dict()
                                for amenity_id in amenities_ids]
        
        # Fetch reviews
        reviews = [self.review_repo.get(review_id).to_dict()
                for review_id in place_dict.get('reviews', [])]
        place_dict['reviews'] = reviews

        return place_dict

    def get_all_places(self):
        # Retrieve all place objects
        places = self.place_repo.get_all()

        # Convert each place to dict and include owner and amenities details
        place_list = []
        for place in places:
            # Ensure place is a Place object before converting to dict
            place_dict = place.to_dict() if not isinstance(place, dict) else place

            owner = self.user_repo.get(place_dict.get('owner_id'))

            if owner:
                place_dict['owner'] = {
                    "id": owner.id,
                    "first_name": owner.first_name,
                    "last_name": owner.last_name,
                    "email": owner.email
                }

            # Ensure 'amenities' key exists and is iterable
            amenities_ids = place_dict.get('amenities', [])
            place_dict['amenities'] = [self.amenity_repo.get(amenity_id).to_dict()
                                    for amenity_id in amenities_ids]

            place_list.append(place_dict)

        return place_list
    
    
    def update_place(self, place_id, place_data):
        # Fetch the existing place
        place = self.place_repo.get(place_id)
        if not place:
            return None

        # Update place's attributes
        place.title = place_data.get('title', place.title)
        place.description = place_data.get('description', place.description)
        place.price = place_data.get('price', place.price)
        place.latitude = place_data.get('latitude', place.latitude)
        place.longitude = place_data.get('longitude', place.longitude)

        # Update the repository
        self.place_repo.update(place_id, place.to_dict())
        return place
    
    def create_review(self, review_data):
        text = review_data.get('text')
        rating = review_data.get('rating')
        place_id = review_data.get('place_id')
        user_id = review_data.get('user_id')

        # Validate place and user existence
        place = self.place_repo.get(place_id)
        user = self.user_repo.get(user_id)
        if not place:
            raise ValueError(f"Place with ID {place_id} not found.")
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        
        # Create and validate the review
        review = Review(text=text, rating=rating, place_id=place_id, user_id=user_id)
        review.validate_rating()
        self.review_repo.add(review)
        
        # Add review to the place
        if not hasattr(place, 'reviews'):
            place.reviews = []
        place.reviews.append(review.id)  # Ensure review ID is stored
        self.place_repo.update(place_id, place.to_dict())

        return review


    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID {review_id} not found.")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def update_review(self, review_id, **kwargs):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID {review_id} not found.")

        if "rating" in kwargs:
            review.rating = kwargs["rating"]
            review.validate_rating()
        if "text" in kwargs:
            review.text = kwargs["text"]

        self.review_repo.update(review_id, review.to_dict())
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID {review_id} not found.")
        self.review_repo.delete(review_id)

    def get_reviews_for_place(self, place_id):
        """Retrieve all reviews for a specific place"""
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError(f"Place with ID {place_id} not found.")
        
        # Assuming reviews are stored as a list of review IDs in the place model
        reviews = [self.review_repo.get(review_id) for review_id in place.reviews]
        return reviews