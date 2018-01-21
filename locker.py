class Locked:
    """
    creates a class for defining the blueprint of all the locked items
    """
    locked_list= []
    """
    new object instances of class Locked will be stored here
    """

    def __init__(self, account, account_password):
        """
        it defines the properties of the class locked
        """

        self.account = account
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


        




