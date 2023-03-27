# Software requirements specification (Vaatimusmäärittely)

## Purpose of the application

The primary purpose of this program is to allow a user to record what exercises they have done at a gym and to track how they have developed overtime in terms of the weights and repetitions. 

The goal is to have a simple application that is nicer to use than Excel, while maintaining a simple UI and without adds or unneccessary functionalities that existing apps are often riddled with.

## User roles

In the initial version there will be only one user type titled "regular user". This way multiple users can have individual profiles on the same computer. 

Depending on the progrss during the course, a superuser role which would be used e.g. by a coach monitoring multiple people could be added.

## Primary functionalities

These functionalities will be implemented as early as possible during the development of the program. 

### Creating a new user or logging in

1. At the beginning there is a choice of either logging in with an existing profile or creating a new one
2. The user can create a new profile
	* The user must choose a username that is at least 4 characters long
	* The program checks that the username is available
	* The user must choose a password that is at least 4 characters long
3. The user can log in into an existing profile
	* The program checks that the username and password match
	* The program gives an error message if the credentials are faulty (username is not registered or password is wrong)

### Using the app as a regular user after logging in

1. The user can choose to add the data from a completed exercise
	* The user adds the date, exercise type, weight and number of repetitions
2. The user can review previous exercises by date
	* The user can edit exercises to correct mistakes
	* The user can remove exercises
3. The user can remove the profile
	* This requires writing the profile's password correctly
4. The user can log out

## Possible future functionalities  

These functionalities will be implemented once the primary functionalities have been completed and if there is time to add more. 

* The user can see high scores for different types of exercises
* The user can set goals 
	* The program marks them completed once an exercise that equals or surpasses the goal is recorded
* The user can see pretty visualizations of their development when viewing previous exercises
* A "coach" superuser can see the exercises completed by all regular users
	* The coach can set new goals to the regular users
	* The coach cannot modify the exercises completed by regular users



