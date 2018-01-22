#!/usr/bin/env python
#python3.7
from signin import User
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
    global username
    global password
    while True:
        print("""\n*********** ^^^ Welcome to Password Locker ^^^ ***********""")
        print("""*** ^^^ Use the keywords provided below to navigate ^^^ ***\n
        signin - create a new account
        login - login into an existing account""")
        keyword = input().lower()

        if keyword == 'signin':
            print("Input your desired username")
            username = input()
            print()

            print("Input your email address")
            email = input()
            print()

            # print("Would you like a password generated for you?")
            # print("Type the - generate - keyword to have a password generated for you\n")

            # if keyword == 'generate':
            #     user = username
            #     generate_password(user)

            # else:
            #     print("Type a password")
              
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
                print("Proceed to login into your account")
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
                print(f"You have successfully logged into your account!")
                print("Enjoy our services!")
                print()
                break                

        elif keyword == 'login':
            print("Input your username")
            username = input()
            print()

            print("Input the password")
            password = input()
            print()

            if username and password:
                print("You have logged in successfully.")
                break                            

        else:
            print()                                 
                                  
    while True:
        print("""**** Use the keywords provided below to navigate through your account **** \n
        create - creating new account details
        display - display all account details 
        find - find an account""")
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
            print("Account creation successful.\n")   

        elif keyword == 'display':
            if display_locked():
                print("\nHere is a list of all your accounts and their details\n")
                for locked in display_locked():
                    print(f'Account name: {locked.account_name}')
                    print(f'username: {locked.username}')
                    print(f'Password: {locked.account_password}')
                    print()
            else:
                print("Sorry... You don't seem to have any saved contacts yet.")
                print()

        elif keyword == 'find':
            print("\nEnter the account name to find the account")
            search_account = input()
            print()
            
            if locked_exists(search_account):
                search_account = find_locked(search_account)
                print(f"Account Name: {search_account.account_name}")
                print(f"Username: {search_account.username}")
                print(f"Password: {search_account.account_password}")
                print()

            else: 
                print("That account does not exist")
                print()

        # elif keyword == 'delete':
        #     print("\nEnter the account name to delete it")
        #     search_account = input()
        #     print()
            
        #     if locked.search_account == locked.username:
        #         delete_locked(locked)
        #         print("Account was successfully deleted\n")

        #     else:
        #         print("Account does not exist\n")

        else: 
            print("You don't have any saved account details yet.\n")

if __name__ == '__main__':
    main()
