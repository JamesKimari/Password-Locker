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



        




