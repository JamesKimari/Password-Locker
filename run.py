#!/usr/bin/env python
#python3.7
from login import User
from locker import Locked
import random
import pyperclip

# user functions

def create_user(username, email, password):
    """
    function to create a new user
    """
    new_user = User(username, email, password)
    return new_user

def save_user(user):
    """
    function to save a new user
    """
    user.save_user()

def generate_password(user):
    """
    function to generate a random password consisting of digits
    based on the user's input
    """
    return user.generate_password()

#locker functions


