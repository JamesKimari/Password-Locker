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

    def tearDown(self):
        """
        this clears up the user_list after each test case has run
        """
        User.user_list = []

    def test_save_user(self):
        """
        this test case checks if the user is added into the user_list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        """
        this test case checks if a user has been deleted form the user_list
        """
        self.new_user.save_user()
        test_user = User("testuser@gmail.com", "testuser")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()

    