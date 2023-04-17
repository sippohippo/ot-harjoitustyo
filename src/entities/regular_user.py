
class RegularUser:
    '''A class for the main user type of the gym app, who records exercises using it.

    Attributes: 

    username:	string, min length 4
    password:	min length 4

    '''

    def __init__(self, username: str, password):
        self.username = username
        self.password = password
