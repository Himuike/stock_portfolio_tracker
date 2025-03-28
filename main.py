# This is the starting point of the program containing main()

from menus.admin_menu import admin_menu
from menus.user_menu import user_menu
from models.user import User

def main():
    while True:
        print("\n**** Welcome ****")
        print("1. New User Registration")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            User.register_user()

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            users = User.load_users()
            if username in users and users[username].password == password:
                if username == "admin":
                    admin_menu()
                else:
                    user_menu(username)
            else:
                print("Invalid username or password.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()