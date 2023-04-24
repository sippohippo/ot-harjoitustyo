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
        weight: None,
        date_of_exercise: str
    ):
        exercise = Exercise(
            exercise_type, set_number, repetitions, weight, date_of_exercise,
            user=self._user.username)

        exercise_added = self._data.add_exercise(
            exercise.id,
            exercise.exercise_type,
            exercise.set_number,
            exercise.repetitions,
            exercise.weight,
            exercise.date_of_exercise,
            exercise.user
        )

        return bool(exercise_added)

    def get_exercises(self):
        pass

    def edit_exercise(self):
        pass

    # User services

    def new_user(self, username, password):
        new_user_created = self._data.add_user(username, password)
        return bool(new_user_created)

    def login(self, username, password):
        credentials = self._data.return_user(username)

        if credentials == (username, password):
            self._user = RegularUser(username, password)
            return True
        return False

    def delete_user(self, username, password):
        credentials = self._data.return_user(username)

        if credentials == (username, password):
            self._data.remove_user(username)
            return True
        return False

        #   print("Invalid password")

    def logout(self):
        pass


exercise_service = ExerciseService(db_tools)
