
import unittest
from entities.exercise import Exercise
from entities.regular_user import RegularUser
from datetime import date


class TestExercise(unittest.TestCase):
    def setUp(self):
        print("")

    def test_exercise_id_works(self):
        exercise1 = Exercise("Barbell Curl", 1, 10, 45.5, "24-04-23")
        exercise_str = str(exercise1)
        date_for_test = "24-04-23"

        self.assertEqual(exercise_str, f"{date_for_test}-Barbell Curl-1")
