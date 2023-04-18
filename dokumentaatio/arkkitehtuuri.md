# Architecture

## Package diagram

[Package diagram](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/packagediagram.png)

## Application logic

The main two classes of the app are RegularUser that represent the users who record exercises and Exercise, which represents the completec exercises during a visit to the gym

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