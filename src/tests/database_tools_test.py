import unittest
from database_tools import db_tools
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


class TestDatabaseTools(unittest.TestCase):
    def setUp(self):
        database_setup()
        db_tools.add_user(test_username, test_password)

    # Tests

    def test_return_user_works(self):
        test_query_result = db_tools.return_user(test_username)
        correct_result = (test_username, test_password)

        self.assertEqual(test_query_result, correct_result)

    def test_adding_exercise_works(self):

        db_tools.add_exercise(test_exercise)

        exercise_type = test_exercise.exercise_type
        set_number = test_exercise.set_number
        repetitions = test_exercise.repetitions
        weight = test_exercise.weight
        date_of_exercise = test_exercise.date_of_exercise
        user = test_exercise.user

        correct_result = [(date_of_exercise, exercise_type,
                           set_number, repetitions, weight)]

        added_exercise_query_result = db_tools.return_exercises(
            test_exercise.user)

        self.assertEqual(correct_result, added_exercise_query_result)

    def test_faulty_exercise_not_added(self):
        pass

    def test_return_exercise_correct_output(self):
        db_tools.add_exercise(test_exercise)
        db_tools.add_exercise(test_exercise2)

        return_exercise_result = db_tools.return_exercises(test_exercise.user)

        exercise_type = test_exercise.exercise_type
        set_number = test_exercise.set_number
        repetitions = test_exercise.repetitions
        weight = test_exercise.weight
        date_of_exercise = test_exercise.date_of_exercise
        user = test_exercise.user

        exercise_type2 = test_exercise2.exercise_type
        set_number2 = test_exercise2.set_number
        repetitions2 = test_exercise2.repetitions
        weight2 = test_exercise2.weight
        date_of_exercise2 = test_exercise2.date_of_exercise
        user2 = test_exercise2.user

        correct_result = [(date_of_exercise, exercise_type, set_number, repetitions, weight),
                          (date_of_exercise2, exercise_type2, set_number2, repetitions2, weight2)]

        self.assertEqual(correct_result, return_exercise_result)

    def test_return_exercise_by_date_correct_output(self):
        exercise_type = test_exercise.exercise_type
        set_number = test_exercise.set_number
        repetitions = test_exercise.repetitions
        weight = test_exercise.weight
        date_of_exercise = test_exercise.date_of_exercise
        user = test_exercise.user

        # Adding 2 exercises, only 1 should be returned
        db_tools.add_exercise(test_exercise)
        db_tools.add_exercise(test_exercise2)

        return_exercise_result = db_tools.return_exercises_by_date(
            test_exercise.user, date_of_exercise)

        correct_result = [(date_of_exercise, exercise_type,
                           set_number, repetitions, weight)]

        self.assertEqual(correct_result, return_exercise_result)

    def test_remove_user_works(self):
        db_tools.remove_user(test_username)
        test_query_result = db_tools.return_user(test_username)
        correct_result = None

        self.assertEqual(test_query_result, correct_result)
