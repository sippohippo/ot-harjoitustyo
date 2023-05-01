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

        exercise_added = self._data.add_exercise(exercise)

        return bool(exercise_added)

    def get_exercises(self):
        exercises = self._data.return_exercises(self._user.username)
        return exercises

    def get_exercises_by_date(self, date):
        exercises = self._data.return_exercises_by_date(
            self._user.username, date)
        return exercises

    def edit_exercise(self, column, new_value, exercise_id):
        edit_successful = self._data.update_exercise(
            column, new_value, exercise_id)
        return edit_successful

    def delete_exercise(self, exercise_id):
        self._data.remove_exercise(exercise_id)

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

    def logout(self):
        self._user = None


exercise_service = ExerciseService(db_tools)
