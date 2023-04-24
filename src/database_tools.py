from database import db_connection

class UserAlreadyExists(Exception):
    pass

class UnableToAddExercise(Exception):
    pass

class DatabaseTools:

    def __init__(self, data):
        self._data = data

    # These queries interact with the exercises table

    def add_exercise(self,
                     exercise_id,
                     exercise_type,
                     set_number,
                     repetitions,
                     weight,
                     date_of_exercise,
                     user):

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
        except UnableToAddExercise:
            return False

    def return_exercises(self):
        pass

    def return_exercise(self):
        pass

    def update_exercise(self):
        pass

    def remove_exercise(self):
        pass

    # These queries interact with the users table

    def add_user(self, username, password):
        cur = self._data.cursor()
        try:
            cur.execute("INSERT INTO users (username,password) VALUES (?,?)", [
                        username, password])
            self._data.commit()
            return True
        except UserAlreadyExists:
            return False

    def return_user(self, username):
        cur = self._data.cursor()
        query_result = cur.execute(
            "SELECT username,password FROM users WHERE username=?", [username]).fetchone()
        return query_result

    def remove_user(self, username):
        cur = self._data.cursor()
        cur.execute("DELETE FROM users WHERE username=?", [username])
        self._data.commit()


db_tools = DatabaseTools(db_connection())
