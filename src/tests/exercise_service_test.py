import unittest
from database_exercise_tools import db_exercise_tools
from database_user_tools import db_user_tools
from database import database_setup
from entities.exercise import Exercise
from services.exercise_service import exercise_service
from entities.regular_user import RegularUser
from services.user_service import user_service


test_exercise = Exercise(
    exercise_type="Barbell Curl",
    set_number=2,
    repetitions=10,
    weight=25.5,
    date_of_exercise="24-04-23",
    user="McTest"
)

test_exercise2 = Exercise(
    exercise_type="Lat Pulldown",
    set_number=2,
    repetitions=10,
    weight=25,
    date_of_exercise="10-04-23",
    user="McTest"
)

test_username = "McTest"
test_password = "1234"


class TestExerciseServices(unittest.TestCase):
    def setUp(self):
        database_setup()
        db_user_tools.add_user(test_username, test_password)
        db_exercise_tools.add_exercise(test_exercise)
        self._ExerciseService = exercise_service
        self._UserService = user_service
        self._UserService.user = RegularUser(test_username, test_password)

    def test_create_exercise_works(self):
        return_value = self._ExerciseService.create_exercise(
            "Barbell Curl", 1, 10, 25.0, "12-12-12")
        self.assertEqual(return_value, True)
