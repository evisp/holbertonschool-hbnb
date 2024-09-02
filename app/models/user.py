from app.models.base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def validate_email(self):
        """Validate email format"""
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(email_regex, self.email):
            raise ValueError("Invalid email format")

    def to_dict(self):
        """Override to_dict to exclude password"""
        user_dict = super().to_dict()
        user_dict.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        })
        return user_dict

    def register(self):
        """Simulate user registration"""
        self.validate_email()
        # Additional registration logic can be added here

    def update_profile(self, first_name=None, last_name=None, email=None, password=None):
        """Update user profile information"""
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
            self.validate_email()
        if password:
            self.password = password

    def delete(self):
        """Simulate user deletion"""
        # Additional deletion logic can be added here
        pass
