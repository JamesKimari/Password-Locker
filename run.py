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
def create_locked(account_name, username, account_password):
    """
    function to create new account details
    """
    new_locked = Locked(account_name, username, account_password)
    return new_locked

def save_locked(locked):
    """
    function to save new locked objects
    """
    locked.save_locked()

def delete_locked(locked):
    """
    function to delete locked objects
    """
    locked.delete_locked()

def find_locked(account_name):
    """
    function to find a locked object by its account name
    """
    return Locked.find_locked(account_name)

def locked_exists(account_name):
    """
    function to check if a locked exists
    """
    return Locked.locked_exists(account_name)

def display_locked():
    """
    function that displays locked objects
    """
    return Locked.display_locked()

def copy_locked(locked):
    """
    function that copies locked object's properties
    """
    return locked.copy_locked(locked)

def main():
    while True:
        print("""\n*********** ^^^ Welcome to Password Locker ^^^ ***********""")
        print("""*** ^^^ Use the keywords provided below to navigate ^^^ ***\n
        login - create a new account
        signin - sign in into an existing account""")
        keyword = input().lower()

        if keyword == 'login':
            print("Input your desired username")
            username = input()
            print()

            print("Input your email address")
            email = input()
            print()

            print("Input a password")
            password = input()
            print()

            print("Confirm your password")
            confirm_password = input()
            save_user(create_user(username, email, password))
            print()
        
            while password != confirm_password:
                print("Incorrect password! Your passwords do not match!")
                print("Please input your password again")
                password = input()
                print()

                print("Confirm your password")
                confirm_password = input()
                print()

            else:
                print(f"You have successfully created a new account!")
                print("Proceed to sign in into your account")
                print("Username")
                signin_username = input()
                print()

                print("password")
                signin_password = input()
                print()

            while signin_username != username or signin_password != password:
                print("Your username or password is incorrect. Please try again...")
                print("username")
                signin_username = input()
                print()

                print("password")
                signin_password = input()
                print()

            else: 
                print(f"You have successfully signed into your account!")
                print("Enjoy our services!")
                print()
                break

        elif keyword == 'signin':
            print("Input your username")
            username = input()
            print()

            print("Input the password")
            password = input()
            print()

            if username and password:
                print("You have signed in successfully.")
                break

        else:
            print("Error. Please use one of the two keyword provided.")

    while True:
        print("""**** Use the keywords provided below to navigate through your account **** \n
        create - creating new account details
        display - display all account details 
        find - find an account
        delete - delete an account """)
        keyword = input().lower()

        if keyword == 'create':
            print("Input the account name")
            account_name = input()
            print()

            print("Input the username")
            username = input()
            print()

            print("Input the account password")  
            account_password = input()
            print() 

            save_locked(create_locked(account_name, username, account_password))     

        elif keyword == 'display':
            print("Here is a list of all your accounts and their passwords\n")
            for locked in display_locked():
                print(f'{locked.account_name} {locked.username} {locked.account_password}\n' )

        else: 
            print("You don't have any saved account details yet.\n")
            break
        
        # elif keyword == 'find':
        #     print("Enter the account name to find the account\n")

if __name__ == '__main__':
    main()

             



    









