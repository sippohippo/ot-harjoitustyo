from services.exercise_service import exercise_service
from entities.regular_user import RegularUser


class GymApplication:
    def __init__(self):
        self._ExerciseService = exercise_service
        self._NotLoggedIn = True

    # THESE FUNCTIONS ARE THE COMMANDS FOR THE INTERFACES

    def login_instructions(self):
        print("Please select one by entering the number:")
        print("1 login to existing user")
        print("2 create new user")
        print("3 quit")

    def main_interface_instructions(self):
        print("")
        print("MAIN MENU")
        print("")
        print("Please select one by entering the number:")
        print("1 add exercise")
        print("2 view and edit past exercises")
        print("3 remove profile")
        print("4 log out")

    def exercise_viewing_instructions(self):
        print("")
        print("VIEWING PAST EXERCISES")
        print("")
        print("Please select one by entering the number:")
        print("1 view all completed exercises")
        print("2 view completed exercises by date")
        print("3 edit an exercise")
        print("4 remove an exercise")
        print("5 back to main menu")

    def add_exercise_instructions(self):
        print("")
        print("Input the name of the exercise (e.g. Barbell Curl)")
        print("Input the set number (e.g. 3)")
        print("Input the number of repetitions (e.g. 10)")
        print("Input the weight with or without decimals (e.g. 20 or 23.5)")
        print("Input the date in DD-MM-YY format (e.g. 25-04-23)")
        print("")

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
        login_successful = self._check_username_and_password()
        if login_successful == True:
            self._NotLoggedIn = False
        else:
            print("")
            print("Invalid username or password")
            print("")

    def _check_username_and_password(self):
        username = input("Username: ")
        password = input("Password: ")
        return exercise_service.login(username, password)

    # THESE FUNCTIONS ARE THE COMMANDS FOR THE MAIN INTERFACE

    def _logout(self):
        confirmation = input("Confirm logout by typing y and pressing enter: ")
        if confirmation == "y":
            self._NotLoggedIn = True
            exercise_service.logout()

    def _remove_user(self):
        print("")
        print("Are you sure you want to remove your account?")
        print("To confirm, please enter your username and password")
        print("")
        login_successful = self._check_username_and_password()
        if login_successful == True:

            # REMOVAL HERE

            print("")
            Print("Profile succesfully removed")
            print("")
            self._NotLoggedIn = True
            exercise_service.logout()

        else:
            print("")
            print("INVALID USERNAME OF PASSWORD!")
            print("")

    def _add_exercise(self):
        self.add_exercise_instructions()
        exercise_type = input("Exercise name: ")
        set_number = input("Set number: ")
        repetitions = input("Number of repeats: ")
        weight = input("Weight (kg): ")
        date = input("Date of exercise (DD-MM-YY) format: ")

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
        while True:
            self.exercise_viewing_instructions()
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
        print("")
        exercises = self._ExerciseService.get_exercises()
        print("Date | Exercise Type | Set | Repetitions | Weight (kg) | Exercise-ID")
        for exercise in exercises:
            print(exercise)

    def _view_exercise_by_date(self):
        print("")
        print("Please provide the date in DD-MM-YY")
        date = input("Date: ")
        print("")
        exercises = self._ExerciseService.get_exercises_by_date(date)
        print("Date | Exercise Type | Set | Repetitions | Weight (kg) | Exercise-ID")
        for exercise in exercises:
            print(exercise)

    def _edit_exercise(self):
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
        pass
