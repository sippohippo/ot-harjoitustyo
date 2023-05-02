from entities.exercise import Exercise
from entities.regular_user import RegularUser
from database_tools import db_tools


class ExerciseService:
    '''Class for the application logic'''

    def __init__(self, data=db_tools):
        self._data = data
        self._user = None
        """The constructor of the class. Creates a database_tools instance.

        Args:
            data: 
                Mandatory. Determines the database that the class is connected to.
                The type is sqlite3.Connection. E.g. sqlite3.connect("exercise_app_database.db").
                Defaults to the one in db_tools.
        """

    def create_exercise(
        self,
        exercise_type: str,
        set_number: int,
        repetitions: int,
        weight: None,
        date_of_exercise: str
    ):
        """Creates a new exercise by using the add_exercise method from database_tools.

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
            user=self._user.username)

        exercise_added = self._data.add_exercise(exercise)

        return bool(exercise_added)

    def get_exercises(self):
        """Gets the user's exercises with the return_exercises method from database_tools.

        Returns:
            A list with tuples that contain the data of each completed exercise.
        """

        exercises = self._data.return_exercises(self._user.username)
        return exercises

    def get_exercises_by_date(self, date):
        """Gets exercises completed on a date using return_exercises_by_date from database_tools.

        Args:
            date: String, the date from which the exercises should be returned.

        Returns: 
            exercises, A list with tuples that contain the data of each completed exercise. 
        """

        exercises = self._data.return_exercises_by_date(
            self._user.username, date)
        return exercises

    def edit_exercise(self, column, new_value, exercise_id):
        """Updates an already completed exercise using the update_exercise from database_tools.
        
        Args:
            columns: String, the name of the variable that holds the value that should be changed.
            new_value: String/Integer/Float the new value that should replace the previous one.
            exercise_id: String, the id used to identify the exercise that should be edited.

        Returns:
            edit_successful that holds True if the edi is successful. False if there is an error.
        """

        edit_successful = self._data.update_exercise(
            column, new_value, exercise_id)
        return edit_successful

    def delete_exercise(self, exercise_id):
        """Deletes an exercise using the remove_exercise method from database_tools.
        
        Args: exercise_id: String, the id used to identify the exercise that should be deleted.
        """

        self._data.remove_exercise(exercise_id)

    def new_user(self, username, password):
        """Creates a new user using the add_user method from database_tools.
        
        Args:
            username: String, the username of the new user.
            password: String, the password of the new user.

        Returns:
            True if the user is successfully added, False if there is an error.
        """

        new_user_created = self._data.add_user(username, password)
        return bool(new_user_created)

    def login(self, username, password):
        """Sets the ExerciseService's user attribute's value to the user logging in and logs in.
        
        Args:
            username: String, the username of the user logging in.
            password: String, the password of the user logging in.      

        Returns:
            True if login is successful, False otherwise.
        """

        credentials = self._data.return_user(username)

        if credentials == (username, password):
            self._user = RegularUser(username, password)
            return True
        return False

    def delete_user(self, username, password):
        """Removes the specified user using the remove_user method from database_tools.
        
        Args:
            username: String, the username of the user that is to be deleted.
            password: String, the password of the user that is to be deleted.            

        Returns:
            True if the deleting of the user is successful, False otherwise.       
        """

        credentials = self._data.return_user(username)

        if credentials == (username, password):
            self._data.remove_user(username)
            return True
        return False

    def logout(self):
        """Logs the user out and sets self._user to None."""

        self._user = None


exercise_service = ExerciseService(db_tools)
