# Architecture

## Package diagram

![Package diagram](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/packagediagram_v2.png)

## Application logic

The main two classes of the app are RegularUser that represent the users who record exercises and Exercise, which represents the completed exercises during a visit to the gym.

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

## Sequence diagrams

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
    UI->>+RegularUser: input("Number of repeats: ")
    RegularUser->>UI: Type a number and press enter
    UI->>+RegularUser: input("Weight (kg): ")
    RegularUser->>UI: Type a number and press enter
    UI->>+RegularUser: input("Date of exercise (DD-MM-YY) format: ")
    RegularUser->>UI: Type a date and press enter    
    
    UI->>ExerciseService: exercise_service.create_exercise(...)
    ExerciseService->>DatabaseTools: add_exercise(exercise)

    DatabaseTools-->>ExerciseService: True
    ExerciseService-->>UI: True

    UI->>+UI: print("Exercise added")
```
