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
        print("")
        print("MAIN MENU")
        print("")
        print("Please select one by entering the number:")
        print("1 add exercise")
        print("2 view past exercises")
        print("3 remove profile")
        print("4 log out")

    def exercise_viewing_instructions(self):
        print("")
        print("VIEWING PAST EXERCISES")
        print("")
        print("Please select one by entering the number:")
        print("1 view all completed exercises")
        print("2 view completed exercises by date")
        print("3 back to main menu")

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
        elif command == str(2):
            self._view_exercises()
        elif command == str(1):
            self._add_exercise()
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

    def _logout(self):
        confirmation = input("Confirm logout by typing y and pressing enter: ")
        if confirmation == "y":
            self._NotLoggedIn = True
            exercise_service.logout()

    def _add_exercise(self):
        print("")
        print("Input the set number and repetitions as numbers like 3 or 10")
        print("Input the weight with or without decimals 20 or 23.5")
        print("Input the date in DD-MM-YY format")
        print("")
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

    def _view_exercises(self):
        while True:
            self.exercise_viewing_instructions()
            print("")
            command = str(input("Command: "))

            if command == str(3):
                break
            elif command == str(2):
                print("")
                print("Please provide the date in DD-MM-YY")
                date = input("Date: ")
                print("")
                exercises = self._ExerciseService.get_exercises_by_date(date)
                print("Date | Exercise Type | Set | Repetitions | Weight (kg)")
                for exercise in exercises:
                    print(exercise)
            elif command == str(1):
                exercises = self._ExerciseService.get_exercises()
                for exercise in exercises:
                    print(exercise)
            else:
                print("Invalind input")




