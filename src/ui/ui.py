from services.exercise_service import exercise_service
from services.user_service import user_service
from entities.regular_user import RegularUser
from tabulate import tabulate
import re


class GymApplication:
    """Class for the text user interface of the program."""

    def __init__(self):
        self._ExerciseService = exercise_service
        self._UserService = user_service
        self._NotLoggedIn = True

    def _login_instructions(self):
        """Used to print the login instructions."""

        print("Please select one by entering the number:")
        print("1 login to existing user")
        print("2 create new user")
        print("3 quit")

    def _main_interface_instructions(self):
        """Used to print the main interface instructions."""

        print("")
        print("MAIN MENU")
        print("")
        print("Please select one by entering the number:")
        print("1 add exercise")
        print("2 view and edit past exercises")
        print("3 remove profile")
        print("4 log out")

    def _exercise_viewing_instructions(self):
        """Used to print the exervice viewing menu's instructions."""

        print("")
        print("VIEWING PAST EXERCISES")
        print("")
        print("Please select one by entering the number:")
        print("1 view all completed exercises")
        print("2 view completed exercises by date")
        print("3 edit an exercise")
        print("4 remove an exercise")
        print("5 back to main menu")

    def _add_exercise_instructions(self):
        """Used to print the exercise adding menu's instructions."""

        print("")
        print("Input the name of the exercise (e.g. Barbell Curl)")
        print("Input the set number (e.g. 3)")
        print("Input the number of repetitions (e.g. 10)")
        print("Input the weight with or without decimals (e.g. 20 or 23.5)")
        print("Input the date in DD-MM-YY format (e.g. 25-04-23)")
        print("")

    def execute(self):
        """Runs the program either in the login ui or main ui."""

        while True:
            print("")
            print("Welcome to the gym training app")
            print(32*"-")

            if self._NotLoggedIn:
                if self._login_ui() == False:
                    break
            else:
                self._main_ui()

    # UIs

    def _login_ui(self):
        """The login menu UI logic."""

        print("")
        self._login_instructions()
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

    def _main_ui(self):
        """The main menu UI logic."""

        print("")
        self._main_interface_instructions()
        print("")
        command = input("Command: ")

        if command == str(4):
            self._logout()
        elif command == str(3):
            self._remove_user()
        elif command == str(2):
            self._view_exercises_menu()
        elif command == str(1):
            self._add_exercise()
        else:
            print("Invalind input")

    def _new_user(self):
        """The UI for adding a new user."""

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

        new_user_created = user_service.new_user(username, password)

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
        """The UI logic for logging in and printing if login fails."""

        login_successful = self._check_username_and_password()
        if login_successful == True:
            self._NotLoggedIn = False
        else:
            print("")
            print("INVALID USERNAME OR PASSWORD")
            print("")

    def _check_username_and_password(self):
        """Used to ask for the username and password and check if it is correct.

        Returns: True if exercise_service.login is succesfull, False otherwise.
        """

        username = input("Username: ")
        password = input("Password: ")
        return user_service.login(username, password)

    # THESE FUNCTIONS ARE THE COMMANDS FOR THE MAIN INTERFACE

    def _logout(self):
        """Confirming log out."""

        confirmation = input("Confirm logout by typing y and pressing enter: ")
        if confirmation == "y":
            self._NotLoggedIn = True
            user_service.logout()

    def _remove_user(self):
        """Removing user logic and UI."""

        print("")
        print("Are you sure you want to remove your account?")
        print("To confirm, please enter your username and password")
        print("")
        username = input("Username: ")
        password = input("Password: ")

        if self._UserService.delete_user(username, password) == True:
            print("")
            print("Profile succesfully removed")
            print("")
            self._NotLoggedIn = True
            user_service.logout()
        else:
            print("")
            print("INVALID USERNAME OR PASSWORD!")
            print("")

    def _add_exercise(self):
        """Adding exercises logic and UI."""

        self._add_exercise_instructions()
        exercise_type = input("Exercise name: ")

        while True:
            set_number = input("Set number: ")
            if self._check_type_of_input(set_number, int):
                break

        while True:
            repetitions = input("Number of repeats: ")
            if self._check_type_of_input(repetitions, int):
                break

        while True:
            weight = input("Weight (kg): ")
            if self._check_type_of_input(weight, float):
                break

        while True:
            date = input("Date of exercise (DD-MM-YY) format: ")
            if self._check_date_format(date):
                break

        added_succesfully = exercise_service.create_exercise(
            exercise_type,
            set_number,
            repetitions,
            weight,
            date
        )

        if added_succesfully == True:
            print("")
            print("Exercise added")
            print("")
        else:
            print("")
            print("Invalid input, please try again")
            print("")

    def _view_exercises_menu(self):
        """Logic for exercise viewing menu."""

        while True:
            self._exercise_viewing_instructions()
            print("")
            command = str(input("Command: "))
            if command == str(5):
                break
            elif command == str(4):
                self._delete_exercise()
            elif command == str(3):
                self._edit_exercise()
            elif command == str(2):
                self._view_exercise_by_date()
            elif command == str(1):
                self._view_exercise()
            else:
                print("Invalind input")

    def _view_exercise(self):
        """Viewing exercises UI and logic."""

        print("")
        exercises = self._ExerciseService.get_exercises()
        print(tabulate(exercises, headers=[
            "Date", "Exercise Type","Set","Repetitions","Weight (kg)","Exercise-ID"],
            tablefmt="github"))

    def _view_exercise_by_date(self):
        """Viewing exercise by date UI and logic."""

        print("")
        print("Please provide the date in DD-MM-YY")
        while True:
            date = input("Date: ")
            if self._check_date_format(date):
                break
        print("")
        exercises = self._ExerciseService.get_exercises_by_date(date)
        print(tabulate(exercises, headers=[
            "Date", "Exercise Type","Set","Repetitions","Weight (kg)","Exercise-ID"], 
            tablefmt="github"))

    def _edit_exercise(self):
        """Editing exercise UI and logic."""

        print("")
        print("What exercise do you want to edit? Please enter the exercise-ID.")
        exercise_id = input("Exercise-ID: ")
        print("")
        print("What parameter do you want to change?")
        print("Possible choices: date_of_exercise, exercise_type, set_number, repetitions, weight")
        column = input("Name of parameter: ")
        print("")
        print("What is the new value to be put into the parameter?")
        new_value = input("New value: ")
        edited_successfully = self._ExerciseService.edit_exercise(
            column, new_value, exercise_id)
        if edited_successfully == True:
            print("")
            print("Edit successful")
            print("")
        else:
            print("")
            print("Invalid input, please try again")
            print("")

    def _delete_exercise(self):
        """Deleting exercise UI and logic."""

        print("")
        print("")
        print("What exercise do you want to delete? Please enter the exercise-ID.")
        exercise_id = input("Exercise-ID: ")
        self._ExerciseService.delete_exercise(exercise_id)
        print("")

    def _check_type_of_input(self, input_value, wanted_type):
        """Checks that an input value is of the correct type."""

        try:
            if isinstance(wanted_type(input_value), wanted_type):
                return True
        except ValueError:
            print("Please use the correct type of input")
            return False

    def _check_date_format(self, date):
        """Checks that a date is in the correct format."""

        correct_format = r'^\d{2}-\d{2}-\d{2}$'
        
        if re.match(correct_format, date):
            return True
        else:
            print("Please follow the suggested date format (DD-MM-YY)")
            return False        

