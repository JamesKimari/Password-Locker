class User:
    """
    creates a class user that acts as a blueprint for all object instances of a user
    """

    user_list = []
    """
    created a list where all new user objects will be stored
    """

    def __init__(self, email, password):
        """
        the __init__ method is for defining the properties of the created class User
        """
    def save_user(self):
        """
        method saves a new user into the user_list
        """
        User.user_list.append(self)


