import unittest
from app import greet


class TestGreeting(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(
            greet("Student"),
            "Hello, Student! Welcome to Git and GitHub."
        )


if __name__ == "__main__":
    unittest.main()