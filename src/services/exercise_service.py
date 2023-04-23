from datetime import date
from entities.exercise import Exercise
from entities.regular_user import RegularUser
from database_tools import db_tools


class ExerciseService:
    '''Class for the application logic'''

    def __init__(self, data=db_tools):
        self._data = data
        self._user = None

    # Exercise services

    def create_exercise(
        self,
        exercise_type: str,
        set_number: int,
        repetitions: int,
        weight: float = None,
        date_of_exercise=date.today(),
        user=None,
    ):

        pass

    def get_exercises(self):
        pass

    def edit_exercise(self):
        pass

    # User services

    def new_user(self, username, password):
        self._data.add_user(username, password)

    def login(self, username, password):
        credentials = self._data.return_user(username)

        if credentials == (username, password):
            self._user = RegularUser(username, password)
        else:
            print("Invalid username or password")

    def delete_user(self, username, password):   
        credentials = self._data.return_user(username)

        if credentials == (username, password):
            self._data.remove_user(username)
        else:
            print("Invalid password")   

    def logout(self):
        pass


exercise_service = ExerciseService(db_tools)
