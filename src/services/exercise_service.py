from entities.exercise import Exercise
from database_exercise_tools import db_exercise_tools
from services.user_service import user_service


class ExerciseService:
    '''Class for the application logic related to handling the Exercise class objects'''

    def __init__(self, exercise_data=db_exercise_tools):
        self._exercise_data = exercise_data
        """Constructor. Creates database_user_tools & database_exercise_tools instances.

        Args:
            exercise_data: 
                Mandatory. Determines the database exercise tools class this class is connected to.
                Defaults to the one in db_exercise_tools.
        """

    def create_exercise(
        self,
        exercise_type: str,
        set_number: int,
        repetitions: int,
        weight: None,
        date_of_exercise: str
    ):
        """Creates a new exercise by using the add_exercise method from database_exercise_tools.

        Args:
            exercise_type: 
                Mandatory.
                String, name of the exercise.
            set_number: 
                Mandatory.
                Integer, the number of the set.
            repetitions: 
                Mandaotry.
                Integer, the number of repetitions.
            weight: 
                Optional, defaults to None.
                Integer/Float, the weight of the used equipment in the exercise.
            date_of_exercise:
                Mandatory.
                String, the date when the exercise was completed.

        Returns:
            True if the exercise is succesfully added. False if there is an error.        
        """

        exercise = Exercise(
            exercise_type, set_number, repetitions, weight, date_of_exercise,
            user=user_service.user.username)

        exercise_added = self._exercise_data.add_exercise(exercise)

        return bool(exercise_added)

    def get_exercises(self):
        """Gets the user's exercises with the return_exercises method from database_exercise_tools.

        Returns:
            A list with tuples that contain the data of each completed exercise.
        """

        exercises = self._exercise_data.return_exercises(
            user_service.user.username)
        return exercises

    def get_exercises_by_date(self, date):
        """Gets exercises from a date with return_exercises_by_date from database_exercise_tools.

        Args:
            date: String, the date from which the exercises should be returned.

        Returns: 
            exercises, A list with tuples that contain the data of each completed exercise. 
        """

        exercises = self._exercise_data.return_exercises_by_date(
            user_service.user.username, date)
        return exercises

    def edit_exercise(self, column, new_value, exercise_id):
        """Updates exercise information using the update_exercise from database_exercise_tools.

        Args:
            columns: String, the name of the variable that holds the value that should be changed.
            new_value: String/Integer/Float the new value that should replace the previous one.
            exercise_id: String, the id used to identify the exercise that should be edited.

        Returns:
            edit_successful that holds True if the edi is successful. False if there is an error.
        """

        edit_successful = self._exercise_data.update_exercise(
            column, new_value, exercise_id)
        return edit_successful

    def delete_exercise(self, exercise_id):
        """Deletes an exercise using the remove_exercise method from database_exercise_tools.

        Args: exercise_id: String, the id used to identify the exercise that should be deleted.
        """

        self._exercise_data.remove_exercise(exercise_id)


exercise_service = ExerciseService(db_exercise_tools)
