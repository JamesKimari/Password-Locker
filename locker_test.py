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

    def test_save_locked(self):
        """
        tests if save_locked method saves the locked object instances
        """
        self.new_locked.save_locked()
        self.assertEqual(len(Locked.locked_list),1)

        
if __name__ == '__main__':
    unittest.main()