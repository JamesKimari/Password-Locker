import pyperclip

class Locked:
    """
    creates a class for defining the blueprint of all the locked items
    """
    locked_list= []
    """
    new object instances of class Locked will be stored here
    """

    def __init__(self, account_name, account_password):
        """
        it defines the properties of the class locked
        """

        self.account_name = account_name
        self.account_password = account_password

    def save_locked(self):
        """
        method for saving the locked_items to the locked_list
        """
        Locked.locked_list.append(self)

    def delete_locked(self):
        """
        method to delete locked objects from the locked_list
        """
        Locked.locked_list.remove(self)

    @classmethod
    def find_locked(cls, account_name):
        """
        The method takes in an account_name and returns a locked 
        object that matches that account_name
        """
        for locked in cls.locked_list:
            if locked.account_name == account_name:
                return locked

    @classmethod
    def locked_exists(cls, account_name):
        """
        method to check if the locked object exists by passing
        in the account_name
        """
        for locked in cls.locked_list:
            if locked.account_name == account_name:
                return True
        return False

    @classmethod
    def display_locked(cls):
        """
        method displays all saved locked objects
        """
        return cls.locked_list

    @classmethod
    def copy_account_password(cls, account_name):
        copy_password = Locked.find_locked(account_name)
        pyperclip.copy(copy_password.account_password)



        




