# This module defines the User class and handles user-related operations.

from utils.file_utils import USERS_FILE

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def load_users():
        users = {}
        with open(USERS_FILE, "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = User(username, password)
        return users

    @staticmethod
    def save_users(users):
        with open(USERS_FILE, "w") as f:
            for username, user in users.items():
                f.write(f"{user.username},{user.password}\n")

    @staticmethod
    def register_user():
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        users = User.load_users()
        if username in users:
            print("Username already exists.")
        else:
            users[username] = User(username, password)
            User.save_users(users)
            print("Registration successful. Please login.")