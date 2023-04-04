
import unittest
from entities.exercise import Exercise
from entities.regular_user import Regular_user
from datetime import date


class TestExercise(unittest.TestCase):
	def setUp(self):
		print("")

	def test_exercise_id_works(self):
		exercise1 = Exercise("Barbell Curl", 1, 10, 45.5)
		exercise_str = str(exercise1)
		date_for_test = date.today()

		self.assertEqual(exercise_str, f"{date_for_test}-Barbell Curl-1")
