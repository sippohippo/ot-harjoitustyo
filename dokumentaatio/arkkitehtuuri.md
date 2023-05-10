# Architecture

## Package diagram

The structure of the program follows the architecture laid out in the package diagram below.

![Package diagram](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/packagediagram_v3.png)

The UI package is self explanatory as it contains the script that houses the user interface. The services package contains the main application logic, which is divided into two separate areas. Lastly, the entities package houses the main classes that are created, manipulated and stored: users and exercises. Left outside of the packages is the main script that executes the program, as well as three helper scripts that contains the initialization of the database and tools for accessing the databases user and exercises tables.

## User interface (UI)

The user interface is a classical text UI that is used through a command line. It consists on multiple different views, or menus, for the different actions. The larger menus are:

* Login menu
* Main menu
* Exercise viewing menu
* Exercise adding menu  

In addition, there are smaller submenus where some inputs are given:

* New user creation 
* View exercise by date 
* Edit exercise 
* Delete exercise 
* Remove user

## Application logic

The main two classes of the app are `RegularUser` that represent the users who record exercises and `Exercise`, which represents the completed exercises during a visit to the gym.

```mermaid
 classDiagram
      Exercise "*" --> "1" RegularUser
      ExerciseService ..> RegularUser
      ExerciseService ..> Exercise
     
      class RegularUser{
          username
          password
      }
      class Exercise{
          
          exercise_type
          set_number
          repetitions
          weight
          date_of_exercise
          user
          id
      }
    class ExerciseService{
       }       

```

The application logic is housed in the services package and more specifically the `ExerciseService` and `UserService` classes. These classes are controlled by inputs given through the UI and provide methods for interacting with the database indirectly through the `DatabaseUserTools` and `DatabaseExerciseTools` classes.

## Sequence diagrams of different functionalities

The sequence diagrams below explain how some critical components of the application logic functions under the hood. 

### Adding an exercise

When a user decides to add a new exercise after logging in and selecting to go to add exercise mode, the following happens:

```mermaid
sequenceDiagram
    Actor RegularUser

    UI->>RegularUser: input("Exercise name: ")
    RegularUser->>UI: Type name and press enter
    UI->>+RegularUser: input("Set number: ")
    RegularUser->>UI: Type a number and press enter
    UI->>+UI: self._check_type_of_input(set_number, int)
    UI->>+RegularUser: input("Number of repeats: ")
    RegularUser->>UI: Type a number and press enter
    UI->>+UI: self._check_type_of_input(repetitions, int)
    UI->>+RegularUser: input("Weight (kg): ")
    RegularUser->>UI: Type a number and press enter
    UI->>+UI: self._check_type_of_input(weight, float)
    UI->>+RegularUser: input("Date of exercise (DD-MM-YY) format: ")
    RegularUser->>UI: Type a date and press enter
    UI->>+UI: self._check_date_format(date)

    UI->>ExerciseService: exercise_service.create_exercise(...)
    ExerciseService->>DatabaseExerciseTools: add_exercise(exercise)

    DatabaseExerciseTools-->>ExerciseService: True
    ExerciseService-->>UI: True

    UI->>+UI: print("Exercise added")
```

The UI asks the user to provide the different values that are stored for the exercise, checking that the right format and type is used. This is then transferred to application logic using the `ExerciseService` class where the method create_exercise(...) is used, with the parameters being the recently asked input values. This create_exercise(...) then uses the add_exercise method from the `DatabaseExerciseTools` class to add the exercise into the program's database. When this is done successfully, both methods return True and then the UI informs the user that the exercise has been added.


### Adding a new user

When the user has chosen to create a new user from the starting menu the following happens in the application logic:

```mermaid
sequenceDiagram
    Actor RegularUser

    UI->>RegularUser: input("Username: ")
    RegularUser->>UI: Type a name and press enter
    UI->>+UI: len(username) >= 4:
    UI->>+RegularUser: input("Password: ")
    RegularUser->>UI: Type a password and press enter
    UI->>+RegularUser: input("Please repeat the password: ")
    RegularUser->>UI: Repeat the previous password and press enter
    UI->>+UI: len(password) >= 4:
    UI->>+UI: password == password_repeat:
    
    UI->>UserService: user_service.new_user(username, password)
    UserService->>DatabaseUserTools: add_user(username, password)

    DatabaseUserTools-->>UserService: True
    UserService-->>UI: True

    UI->>+UI: print("New user created")
```

The UI asks the user to provide a username and checks that it is at least 4 characters long. Then it asks the user to provide a password and to repeat it, checking that the length is at least 4 characters and that the password and repeat match. Once these conditions are met, the UI uses the `UserService` class and its new_user(...) method with the username and password as parameters. This in turn calls the add_user method of the `DatabaseUserTools` class to enter the new user to the program's database. These then return True one after another assuming the adding of the user was successful and finally the UI informs the user of the account having been created.

### Logging in

When the user has selected to log in to an existing account in the starting menu the following happens in the application logic:

```mermaid

sequenceDiagram
    Actor RegularUser

    UI->>+UI: self._check_username_and_password()
    UI->>RegularUser: input("Username: ")
    RegularUser->>UI: Type the username and press enter
    UI->>+RegularUser: input("Password: ")
    RegularUser->>UI: Type the password and press enter
    UI->>UserService: user_service.login(username, password)
    UserService->>DatabaseUserTools: return_user(username)
    DatabaseUserTools-->>UserService: credentials
    UserService->>UserService: credentials == (username, password)
    UserService->>UserService: user = RegularUser(username, password)
    UserService-->>UI: True
    UI->>+UI: self._NotLoggedIn = False

```

The UI calls its own method check_username_and_password() which in turn prompts the user to their username and password. Then, the UI uses the `UserService` class and its login() method giving the username and password as parameters. Then, `UserService` uses the `DatabaseUserTools` class and its method return_user to get from the database the username and password storing it as a tuple to "credentials", which is then compared to the username and password provided by the user. If they match, in `UserService` the user variable is set to RegularUser(username, password) and then `UserService` returns the value True to the UI. Then the UI sets its variable NotLoggedIn to False.

## Data storage

### High-level description

The data, which in this case is information on the users and exercises done by the users are stored in a SQLite database. These are stored in respectively named tables. The relational schema below shows the column names as well as relationship between the two tables.

![Relational Schema](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/rschema.png)

As can be seen, the username is a foreign key in the exercises table. Each user can have many exercises, but each exercise can have only one user. 

### DatabaseExerciseTools and DatabaseUserTools classes

The `DatabaseExerciseTools` and `DatabaseUserTools` classes are used by the `ExerciseService` class and `UserService` class to directly interact and manipulate the database. This way the program logic is separated from the database more explicitly. Note that both of these database tools classes are stored outside of the packages in the main src directory in the file [database_user_tools.py](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/database_user_tools.py) and [database_exercise_tools.py](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/database_exercise_tools.py). 


# Known flaws in the current architecture

As this is primarily designed for personal use, it does not take into consideration the fact that in the database there will be a problem if two separate users were to record the exact same exercise, as these would not be unique. This could be fixed by adding an additional ID column.

