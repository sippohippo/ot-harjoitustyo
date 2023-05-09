# Testing document

## Unit testing

Most testing in this project is done with the standard Python unittest unit testing framework. Below is a list of the files and the classes which they test

- [database_exercise_tools_test](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/database_exercise_tools_test.py) contains the tests for the class `DatabaseExerciseTools`
- [database_user_tools_test](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/database_user_tools_test.py) constains the tests for the class `DatabaseUserTools`
- [exercise_service_test](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/exercise_service_test.py) constains the tests for the class `ExerciseService`
- [user_service_test](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/user_service_test.py) constains the tests for the class `UserService`
- [exercise_test.py](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/exercise_test.py) constains the tests for the class `Exercise`
- [regular_user_test.py](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/regular_user_test.py) constains the tests for the class `RegularUser`

## Integration testing

Some of the files listed above contain also integration tests that test a combination of the different packages of the program. These are:

- [exercise_service_test](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/exercise_service_test.py) which tests the `ExerciseService` class, and thus also tests the integration of `ExerciseService` with `DatabaseExerciseTools`
- [user_service_test](https://github.com/sippohippo/ot-harjoitustyo/blob/master/src/tests/user_service_test.py) which tests the `UserService` class, and thus also tests the integration of `UserService` with `DatabaseUserTools`

Further integration testing was done manually, as no automatic tests were made for the UI. By runnign the program and testing all the different functionalities, the integration between the class `GymApplication` (which contains the UI) and the services and database tools classes was tested.

## System testing

The program has been manually tested on both macOS (ver 13.3.1 (22E261)) and Linux (Cubbli-Linux). Testing was done both by using the releases as well as by cloning the most recent version of the repository.

## Coverage


## Known bugs

