import unittest
from locker import Locked

class TestLocked(unittest.TestCase):
    def setUp(self):
        """
        SetUp method to run before each test
        """
        self.new_locked = Locked("Password Locker", "emmawatson")

    def test_init(self):
        """
        checks if the instance variables are instantiated correctly
        """
        self.assertEqual(self.new_locked.account, "Password Locker")
        self.assertEqual(self.new_locked.account_password, "emmawatson")
        
if __name__ == '__main__':
    unittest.main()