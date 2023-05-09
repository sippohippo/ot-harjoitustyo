import sqlite3
from database import db_connection


class DatabaseExerciseTools:
    """This class is responsible for all interactions with the sqlite database's exercise table"""

    def __init__(self, data):
        self._data = data
        """The constructor of the class. Creates a database_tools instance.

        Args:
            data: 
                Mandatory. Determines the database that the class is connected to.
                The type is sqlite3.Connection. E.g. sqlite3.connect("exercise_app_database.db").
        """

    def add_exercise(self, exercise):
        """Adds a new row to the exercises table in the database.

        Args:
            exercise: Exercise class object, an exercise to be added to the database.

        Returns:
            True if the row is succesfully added. False if there is an error.

        Raises:
            sqlite3.OperationalError: An error if the row cannot be added to the database.    
        """

        exercise_id = exercise.id
        exercise_type = exercise.exercise_type
        set_number = exercise.set_number
        repetitions = exercise.repetitions
        weight = exercise.weight
        date_of_exercise = exercise.date_of_exercise
        user = exercise.user

        cur = self._data.cursor()
        try:
            cur.execute('''INSERT INTO exercises (
                        id,
                        exercise_type,
                        set_number,
                        repetitions,
                        weight,
                        date_of_exercise,
                        exercise_username) 
                        VALUES (?,?,?,?,?,?,?)''', [exercise_id,
                                                    exercise_type,
                                                    set_number,
                                                    repetitions,
                                                    weight,
                                                    date_of_exercise,
                                                    user]
                        )
            self._data.commit()
            return True
        except sqlite3.OperationalError:
            return False

    def return_exercises(self, username):
        """Retrieves all exercises belonging to the user.

        Args:
            username: String, the name of the user whose exercises are retrieved.

        Returns:
            A list with tuples that contain the data of each completed exercise.
        """

        cur = self._data.cursor()
        query_result = cur.execute(
            '''SELECT 
            date_of_exercise, exercise_type, set_number, repetitions, weight, id 
            FROM exercises WHERE exercise_username=?''', [username]).fetchall()
        return query_result

    def return_exercises_by_date(self, username, date):
        """Retrieves all exercises that have a specific date.

        Args:
            username: String, the name of the user whose exercises are retrieved.
            date: String, the date from which the exercises should be returned.

        Returns: 
            A list with tuples that contain the data of each completed exercise. 
        """

        cur = self._data.cursor()
        query_result = cur.execute(
            '''SELECT 
            date_of_exercise, exercise_type, set_number, repetitions, weight, id 
            FROM exercises 
            WHERE exercise_username=? AND date_of_exercise=?''', [
                username, date]).fetchall()
        return query_result

    def update_exercise(self, column, new_value, exercise_id):
        """Updates the data from an already existing exercise.

        Args:
            column: String, name of the column storing the value that should be updated.
            new_value: String/Integer/float, the value that replaces the old value.
            exercise_id: String, the unique id used to identify the row where the value is changed.

        Returns:
            True if the row is succesfully edited. False if there is an error.

        Raises:
            sqlite3.OperationalError: An error if the row cannot be updated in the database
        """

        cur = self._data.cursor()

        try:
            cur.execute(
                f'''UPDATE EXERCISES SET {column} = {new_value} WHERE id="{exercise_id}"''')
            self._data.commit()
            return True
        except sqlite3.OperationalError:
            return False

    def remove_exercise(self, exercise_id):
        """Removes an exercise from the exercises table

        Args:
            exercise_id: The unique identifier for the exercise
        """

        cur = self._data.cursor()
        cur.execute("DELETE FROM exercises WHERE id=?", [exercise_id])
        self._data.commit()


db_exercise_tools = DatabaseExerciseTools(db_connection())
