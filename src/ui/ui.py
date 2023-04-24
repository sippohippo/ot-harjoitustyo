from services.exercise_service import exercise_service
from entities.regular_user import RegularUser


class GymApplication:
    def __init__(self):
        self._ExerciseService = exercise_service
        self._NotLoggedIn = True

    def login_instructions(self):
        print("Please select one by entering the number:")
        print("1 login to existing user")
        print("2 create new user")
        print("3 quit")

    def main_interface_instructions(self):
        print("MAIN MENU")
        print("")
        print("Please select one by entering the number:")
        print("1 add exercise")
        print("2 view past exercises")
        print("3 remove profile")
        print("4 log out")

    def execute(self):
        while True:
            print("")
            print("Welcome to the gym training app")
            print(32*"-")

            if self._NotLoggedIn:
                if self.login_ui() == False:
                    break
            else:
                self.main_ui()

    # UIs

    def login_ui(self):
        print("")
        self.login_instructions()
        print("")
        command = input("Command: ")

        if command == str(3):
            return False
        elif command == str(2):
            self._new_user()
        elif command == str(1):
            self._login()
        else:
            print("Invalind input")

    def main_ui(self):
        print("")
        self.main_interface_instructions()
        print("")
        command = input("Command: ")

        if command == str(4):
            self._NotLoggedIn = True
        else:
            print("Invalind input")

    # THESE FUNCTIONS ARE THE COMMANDS FOR THE LOGIN INTERFACE

    def _new_user(self):
        print("What username do you want? Minimum length is 4 characters")

        while True:
            username = input("Username: ")
            if len(username) >= 4:
                break
            else:
                print("Please choose a username that is at least 4 characters long")

        print("Please choose a password that is at least 4 characters long")

        while True:
            password = input("Password: ")
            password_repeat = input("Please repeat the password: ")

            if len(password) < 4:
                print("Please choose a password that is at least 4 characters long")
            if password != password_repeat:
                print("Passwords do not match, please try again")
            if password == password_repeat and len(password) >= 4:
                break

        new_user_created = exercise_service.new_user(username, password)

        if new_user_created == True:
            print("New user created")
            print("")
            print("Please login to your new account.")
            self._login()
        else:
            print("")
            print("Username already taken. Please choose another one!")
            print("")
            self._new_user()

    def _login(self):
        print("")
        username = input("Username: ")
        password = input("Password: ")
        login_successful = exercise_service.login(username, password)
        if login_successful == True:
            self._NotLoggedIn = False
        else:
            print("")
            print("Invalid username or password")
            print("")

    # THESE FUNCTIONS ARE THE COMMANDS FOR THE MAIN INTERFACE
