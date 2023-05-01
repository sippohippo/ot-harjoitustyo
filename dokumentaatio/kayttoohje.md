# User guide

## Downloading the application

This application can be downloaded either as a zip file from the Releases section or by cloning the repository. Cloning the repository will give access to the latest features, while the releases are more stable and less likely to have bugs.

Cloning can be done by opening the terminal (command line) and entering:

```bash
git clone https://github.com/sippohippo/ot-harjoitustyo
```

The downloadable releases can be found by clicking [here](https://github.com/sippohippo/ot-harjoitustyo/releases.).


## Setup

After downloading the the release and opening the zip file or after cloning the repository, go to the same directory on the command line. 

Make sure that you have Python (3.8 or higher) and Poetry installed. The dependencies of the program can be installed using the terminal with:

```bash
poetry install
```

Next, before opening the application for the first, you must initiliaze the database where the users and exercises will be stored. This is done by entering the following command in the terminal:

```bash
poetry run invoke build
```

## Starting the application

Before going to this step, remember that if this is the first time you are using the application, you need to go through the steps outlined in the **Setup** section above first.

If the setup has already been done, you can start using the application. To start the app, type the following command into the terminal:

```bash
poetry run invoke start
```

## Creating a new user

Before using the program you need to have a user. You can create a new user with the command 2 (type 2 and press enter). Follow the instructions and type in the username, password and repeat the password once more to create the account. If the username has not been taken and the username and password meet the requirements (at least 4 characters long) you will receive a notification that the account has been created and you will be asked to log in to the account.

## Logging in and out

To log in to an existing user, type 1 and press enter in the starting screen. First you will need to type your username and then press enter and then your password and then press enter. 

After being logged in, it is possible to log out with the command 5. Type 5 and press enter and then you will be asked to confirm this by typing y and pressing enter. Any other command will return you back to the main menu and not log you out. 

## Adding exercises

To add exercises, use the command 1 and press enter in the main menu. Then you will be asked to enter the information about the completed exercise one at a time. Please follow the instructions given to you at each step. 

## Viewing and editing past exercises

First go to the *view and edit past exercises* view with the command 2 and by pressing enter. This takes you to a new menu.

### Viewing previous exercises

To view previous exercises, use the command 1 or 2 and press enter in the main menu. With command 1 you will simply get a list of all completed exercises in the order which they have been entered.

With command 2 you will be asked to provide a date and then the program will print out all exercises completed on that day.

### Editing past exercises

To edit previous exercises, use the command 3 and press enter.

### Deleting past exercises

To delete previous exercises, use the command 4 and press enter.

# For developers

If you are intending to further develop this program, below is a list of useful commands that have already been defined that you can use:

Run tests with:

```bash
poetry run invoke test
```

Generate a test coverage report with:

```bash
poetry run invoke coverage-report
```

Check that the code follows the format specified with Pylint with:

```bash
poetry run invoke lint
```
