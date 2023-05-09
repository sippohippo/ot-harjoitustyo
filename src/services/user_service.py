from entities.regular_user import RegularUser
from database_user_tools import db_user_tools


class UserService:
    '''Class for the application logic related to handling the User class objects'''

    def __init__(self, data=db_user_tools):
        self._data = data
        self.user = None

        """The constructor of the class. Creates a database_tools instance.

        Args:
            data: 
                Mandatory. Determines the database user tools class this class is connected to.
                Defaults to the one in db_user_tools.
        """

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
            self.user = RegularUser(username, password)
            return True
        return False

    def logout(self):
        """Logs the user out and sets self._user to None."""

        self.user = None

    def new_user(self, username, password):
        """Creates a new user using the add_user method from database_user_tools.

        Args:
            username: String, the username of the new user.
            password: String, the password of the new user.

        Returns:
            True if the user is successfully added, False if there is an error.
        """

        new_user_created = self._data.add_user(username, password)
        return bool(new_user_created)

    def delete_user(self, username, password):
        """Removes the specified user using the remove_user method from database_user_tools.

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


user_service = UserService(db_user_tools)
