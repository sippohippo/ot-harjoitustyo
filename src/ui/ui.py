from services.exercise_service import exercise_service


class GymApplication:
    def __init__(self):
        self.__ExerciseService = exercise_service

    def login_instructions(self):
        print("Please select one:")
        print("1 login to existing user")
        print("2 create new user")
        print("3 quit")

    def main_interface_instructions(self):
        pass

    def execute(self):
        print("")
        print("Welcome to the gym training app")
        print(32*"-")

        while True:
            print("")
            self.login_instructions()
            print("")
            command = int(input("Command: "))

            if command == 3:
                break
            elif command == 2:
                self._new_user()
            elif command == 1:
                self._login()
            else:
                print("Invalind input")
                print("")
                self.login_instructions()


    def _new_user(self):
        username = input("Username: ")
        password = input("Password: ")
        password_repeat = input("Please repeat the password: ")

        if password == password_repeat:
            exercise_service.new_user(username,password)
            self._login()
        else:
            print("Passwords do not match, please try again")
            self._new_user()

    def _login(self):
        username = input("Username: ")
        password = input("Password: ")
        exercise_service.login(username,password)

