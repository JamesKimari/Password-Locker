import unittest
from login import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        The setUp method runs before each test
        """

        self.new_user = User("jamesgkimari@gmail.com", "emmawatson")

    def test_init(self):
        """
        this checks if all the instance variables are instantiated correctly
        """
        self.assertEqual(self.new_user.email, "jamesgkimari@gmail.com")
        self.assertEqual(self.new_user.password, "emmawatson")


if __name__ == '__main__':
    unittest.main()

    