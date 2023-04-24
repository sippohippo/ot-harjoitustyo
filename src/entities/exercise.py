
class Exercise:
    '''A class that represents individual exercises completed by the regular user.

    Attributes:

    exercise_type:	   string, name of exercise (e.g pushup)
    set_number:        int, number of the set, e.g. 1 (out of 3 if doing a set of 3)
    repetitions:	   int, number of times the move was repeated (e.g. 10 pushups)
    weight:			   float, optional, when using equipment with specific weights
    date_of_exercise:  str representation of the date (DD-MM-YY)
    user:			   the regular_user who the exercise belongs to
    id:			       unique id used for retrieving individual exercises later

    '''

    def __init__(
        self,
        exercise_type: str,
        set_number: int,
        repetitions: int,
        weight: float = None,
        date_of_exercise=str,
        user=None,
    ):
        '''Constructor

        Args:

        exercise_type:	    string
        repetitions:	    int
        set_number:	    	int
        weight:			    float (optional), defaultsto None
        date_of_exercise:	str
        user:		     	User class object, optional, defaults to None

        '''

        self.exercise_type = exercise_type
        self.set_number = set_number
        self.repetitions = repetitions
        self.weight = weight
        self.date_of_exercise = date_of_exercise
        self.user = user
        self.id = f"{date_of_exercise}-{exercise_type}-{set_number}"

    def __str__(self):
        return self.id
