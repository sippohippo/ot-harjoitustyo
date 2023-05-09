import unittest
from database_exercise_tools import db_exercise_tools
from database_user_tools import db_user_tools
from database import database_setup
from entities.exercise import Exercise


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


class TestDatabaseUserTools(unittest.TestCase):
    def setUp(self):
        database_setup()
        db_user_tools.add_user(test_username, test_password)

    # Tests

    def test_return_user_works(self):
        test_query_result = db_user_tools.return_user(test_username)
        correct_result = (test_username, test_password)

        self.assertEqual(test_query_result, correct_result)

    def test_remove_user_works(self):
        db_user_tools.remove_user(test_username)
        test_query_result = db_user_tools.return_user(test_username)
        correct_result = None

        self.assertEqual(test_query_result, correct_result)
