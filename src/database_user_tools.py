import sqlite3
from database import db_connection


class DatabaseUserTools:
    """This class is responsible for all interactions with the sqlite database's user table"""

    def __init__(self, data):
        self._data = data
        """The constructor of the class. Creates a database_tools instance.

        Args:
            data: 
                Mandatory. Determines the database that the class is connected to.
                The type is sqlite3.Connection. E.g. sqlite3.connect("exercise_app_database.db").
        """

    def add_user(self, username, password):
        """This adds a new user to the user table.

        Args:
            username: String, the username to be put in the new row.
            password: String, the password to be put in the new row.

        Returns:
            True if the row is succesfully added. False if there is an error.

        Raises:
            sqlite3.IntegrityError: An error if the row cannot be added to the database.
        """

        cur = self._data.cursor()
        try:
            cur.execute("INSERT INTO users (username,password) VALUES (?,?)", [
                        username, password])
            self._data.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def return_user(self, username):
        """Retrieves the username and password of a user

        Args:
            username: String, the username to be searched for.
        Returns:
            A tuple with the username and password.
        """

        cur = self._data.cursor()
        query_result = cur.execute(
            "SELECT username,password FROM users WHERE username=?", [username]).fetchone()
        return query_result

    def remove_user(self, username):
        """Removes a user from the users table

        Args:
            username: String, the user that is to be removed
        """

        cur = self._data.cursor()
        cur.execute(
            "DELETE FROM exercises WHERE exercise_username=?", [username])
        cur.execute("DELETE FROM users WHERE username=?", [username])
        self._data.commit()


db_user_tools = DatabaseUserTools(db_connection())
