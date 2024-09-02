import pytest
from app.models.review import Review

def test_review_creation():
    review = Review(text="Excellent stay!", rating=5, place_id="some-place-id", user_id="some-user-id")
    assert review.text == "Excellent stay!"
    assert review.rating == 5

def test_review_invalid_rating():
    with pytest.raises(ValueError, match="Rating must be between 1 and 5"):
        review = Review(text="Bad stay", rating=6, place_id="some-place-id", user_id="some-user-id")
        review.validate_rating()

test_review_creation()

