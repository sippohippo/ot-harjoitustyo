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


class TestDatabaseExerciseTools(unittest.TestCase):
    def setUp(self):
        database_setup()
        db_user_tools.add_user(test_username, test_password)

    # Tests

    def test_adding_exercise_works(self):

        db_exercise_tools.add_exercise(test_exercise)

        exercise_type = test_exercise.exercise_type
        set_number = test_exercise.set_number
        repetitions = test_exercise.repetitions
        weight = test_exercise.weight
        date_of_exercise = test_exercise.date_of_exercise
        user = test_exercise.user
        exercise_id = test_exercise.id

        correct_result = [(date_of_exercise, exercise_type,
                           set_number, repetitions, weight, exercise_id)]

        added_exercise_query_result = db_exercise_tools.return_exercises(
            test_exercise.user)

        self.assertEqual(correct_result, added_exercise_query_result)

    def test_faulty_exercise_not_added(self):
        pass

    def test_return_exercise_correct_output(self):
        db_exercise_tools.add_exercise(test_exercise)
        db_exercise_tools.add_exercise(test_exercise2)

        return_exercise_result = db_exercise_tools.return_exercises(
            test_exercise.user)

        exercise_type = test_exercise.exercise_type
        set_number = test_exercise.set_number
        repetitions = test_exercise.repetitions
        weight = test_exercise.weight
        date_of_exercise = test_exercise.date_of_exercise
        user = test_exercise.user
        exercise_id = test_exercise.id

        exercise_type2 = test_exercise2.exercise_type
        set_number2 = test_exercise2.set_number
        repetitions2 = test_exercise2.repetitions
        weight2 = test_exercise2.weight
        date_of_exercise2 = test_exercise2.date_of_exercise
        user2 = test_exercise2.user
        exercise_id2 = test_exercise2.id

        correct_result = [(date_of_exercise, exercise_type, set_number, repetitions, weight, exercise_id),
                          (date_of_exercise2, exercise_type2, set_number2, repetitions2, weight2, exercise_id2)]

        self.assertEqual(correct_result, return_exercise_result)

    def test_return_exercise_by_date_correct_output(self):
        exercise_type = test_exercise.exercise_type
        set_number = test_exercise.set_number
        repetitions = test_exercise.repetitions
        weight = test_exercise.weight
        date_of_exercise = test_exercise.date_of_exercise
        user = test_exercise.user
        exercise_id = test_exercise.id

        # Adding 2 exercises, only 1 should be returned
        db_exercise_tools.add_exercise(test_exercise)
        db_exercise_tools.add_exercise(test_exercise2)

        return_exercise_result = db_exercise_tools.return_exercises_by_date(
            test_exercise.user, date_of_exercise)

        correct_result = [(date_of_exercise, exercise_type,
                           set_number, repetitions, weight, exercise_id)]

        self.assertEqual(correct_result, return_exercise_result)
