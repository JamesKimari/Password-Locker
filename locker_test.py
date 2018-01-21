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

    def tearDown(self):
        """
        cleans up the locked_list after each test run
        """
        Locked.locked_list = []

    def test_delete_locked(self):
        """
        test case to test whether the delete_locked method works
        """
        self.new_locked.save_locked()
        test_locked = Locked("Facebook", "lolest")
        test_locked.save_locked()
        self.new_locked.delete_locked()
        self.assertEqual(len(Locked.locked_list),1)

if __name__ == '__main__':
    unittest.main()