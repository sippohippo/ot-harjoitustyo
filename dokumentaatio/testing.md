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

The program has been manually tested on both macOS (ver 13.3.1 22E261) and Linux (Cubbli-Linux). Testing was done both by using the releases as well as by cloning the most recent version of the repository.

In the manual tests all major features were tested that they work as intended and most common attempts to type something wrong will not crash the program or cause bugs. This includes checking that the UI works as intended on both macOS and Linux terminals. Note that this application has not been tested in a Windows operating system and may not function even when e.g. using Windows Subsystem for Linux (WSL).

## Coverage report

![Coverage report](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/final_coverage.png)


## Known bugs

- Running the tests reinitializes the database. This means any data saved in it will be lost. Thus the intended end user of this program should not be running the tests after starting to use the program to record exercises.

- There is no strict enforcing of types in the database. When editing exercises it is possible to input weird values into some of the variables. However, when adding new exercises it is not possible to input wrong values.

