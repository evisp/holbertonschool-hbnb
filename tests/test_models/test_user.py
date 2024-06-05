import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(email="test@example.com", first_name="Test", last_name="User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_user_update(self):
        user = User(email="test@example.com", first_name="Test", last_name="User")
        user.update(first_name="Updated")
        self.assertEqual(user.first_name, "Updated")
        self.assertIsNotNone(user.updated_at)

if __name__ == '__main__':
    unittest.main()
