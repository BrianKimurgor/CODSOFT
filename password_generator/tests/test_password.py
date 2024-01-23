import unittest
from unittest.mock import patch
from password import generate_password
import string

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_length(self):
        # Test if the generated password has the correct length
        length = 8
        password = generate_password(length)
        self.assertEqual(len(password), length)

    @patch('builtins.input', side_effect=['12'])
    def test_generate_password_input(self, mock_input):
        # Test if the function handles user input correctly
        password = generate_password(8)
        self.assertEqual(len(password), 8)

    def test_generate_password_invalid_input(self):
        # Test if the function handles invalid input correctly
        with patch('builtins.input', side_effect=['abc', '8']):
            password = generate_password(8)
            self.assertEqual(len(password), 8)

    def test_generate_password_special_characters(self):
        # Test if the generated password contains at least one special character
        length = 10
        password = generate_password(length)
        self.assertTrue(any(char in string.punctuation for char in password))

if __name__ == '__main__':
    unittest.main()
