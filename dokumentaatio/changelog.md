# Changelog

## Week 3

- Created the class Regular_user
- Created the class Exercise that records individual completed exercises
- Added tests to check that the Exercise class works properly
- Created a template for the class Exercise_Service which will contain the application logic

## Week 4

- Renamed Regular_user to RegularUser
- Added pylint to the project and fixed style issues such as indents vs spaces
- First version of database and script for initializing database added
- Added script for interacting with the database
- Updated program logic
- Added first rough text-UI
- Added architecture schematics

## Week 5

- Updated program logic and database tools
- Removed all printing outside of UI
- Creating new accounts and logging in and out now works as intended
- First version of main logged in UI created
- Removed use of date module and replaced with str
- Added the ability to add exercises
- Added the ability to view exercises (all or filtering by date)
- Added tests for all database_tools functions except for exception branches

## Week 6

- User guide added
- Created new method for checking log in to avoid repeating code
- Ability to edit exercises added
- Ability to remove profile added
- Tests for exercise_service added
- Docstring to exercise_service added
- Docstring to database_tools added 
- Docstring to ui added
- Architecture description expanded
- V2 released

## Week 7

- Separated the ExerciseService class into two separate classes: ExerciseService and UserService
- Separated the DatabaseTools class into two separate classes: DatabaseExerciseTools and DatabaseUserTools
- Updated tests to match the new divided classes
- Updated documentation to match new classes
- Added tabulate library to print the exercises more elegantly in the UI
- Testing doc added
- Added validation of inputs when adding exercises
- Architecture description updated and new diagrams added