
import unittest
from entities.exercise import Exercise
from entities.regular_user import RegularUser
from datetime import date


class TestExercise(unittest.TestCase):
    def setUp(self):
        print("")

    def test_exercise_id_works(self):
        exercise1 = Exercise("Barbell Curl", 1, 10, 45.5)
        exercise_str = str(exercise1)
        date_for_test = date.today()

        self.assertEqual(exercise_str, f"{date_for_test}-Barbell Curl-1")


class TestRegularUser(unittest.TestCase):
    def setUp(self):
        print("")

    def test_regular_user_attributes_work(self):

        test_user = RegularUser("Hippo", "salari123")

        self.assertEqual(
            (test_user.username, test_user.password), ("Hippo", "salari123"))
