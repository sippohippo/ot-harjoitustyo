from services.exercise_service import ExerciseService


class GymApplication:
    def __init__(self):
        self.__ExerciseService = ExerciseService()

    def login_instructions(self):
        print("Available commands:")
        print("1 login to existing user")
        print("2 create new user")
        print("3 quit")

    def main_interface_instructions(self):
        pass

    def execute(self):
        self.login_instructions()

        while True:
            print("")
            command = int(input("Command: "))

            if command == 3:
                break
            elif command == 2:
                self.new_user()
            elif command == 1:
                self.login()
            else:
                print("Invalind input")
                print("")
                self.login_instructions()

#    	while True:


# application = GymApplication()
# application.execute()
