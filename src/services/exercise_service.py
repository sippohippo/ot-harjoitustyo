
from entities.exercise import Exercise
from entities.regular_user import Regular_user


class ExerciseService:
	'''Class for the application logic'''


	# Exercise services

	def create_exercise(exercise_type: str, set_number: int, repetitions: int, weight: float=None, date=date.today(), user=None, id=None):
		pass

	def get_exercises(self):
		pass

	def edit_exercise(self):
		pass


	# User services

	def new_user(self, username, password):
		pass

	def login(self, username, password):
		pass

	def logout(self):
		pass