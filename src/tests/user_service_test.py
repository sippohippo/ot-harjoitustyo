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

class TestUserServices(unittest.TestCase):
    def setUp(self):
        database_setup()
        db_user_tools.add_user(test_username, test_password)
        db_exercise_tools.add_exercise(test_exercise)
        self._ExerciseService = exercise_service
        self._UserService = user_service
        self._UserService.user = RegularUser(test_username, test_password)

    def test_login_correct_credentials_works(self):
        return_value = self._UserService.login("McTest", "1234")
        self.assertEqual(return_value, True)

    def test_login_wrong_credentials_works(self):
        return_value = self._UserService.login("McTest", "Wrong_password")
        self.assertEqual(return_value, False)