from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    def validate_rating(self):
        """Ensure rating is between 1 and 5"""
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

    def to_dict(self):
        """Override to_dict to include place and user ids"""
        review_dict = super().to_dict()
        review_dict.update({
            "text": self.text,
            "rating": self.rating,
            "place_id": self.place_id,
            "user_id": self.user_id
        })
        return review_dict
