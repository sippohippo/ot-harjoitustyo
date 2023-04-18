
import sqlite3

database = sqlite3.connect("exercise_app_database.db")
cursor = database.cursor()


def database_setup():
    '''
    This function contains the coded needed to initializes the database 
    '''

    cursor.execute("drop table if exists exercises;")
    cursor.execute("drop table if exists users;")

    # Creating the table for storing users

    cursor.execute("""create table users (
        username TEXT PRIMARY KEY,
        password TEXT
        );
    """)

    database.commit()

    # Creating the table for storing exercises

    cursor.execute("""create table exercises (
        id TEXT PRIMARY KEY,
        exercise_type TEXT,
        set_number INTEGER,
        repetitions INTEGER,
        weight REAL,
        date_of_exercise DATE,
        exercise_username TEXT, 
        FOREIGN KEY(exercise_username) REFERENCES users(username)
        );
    """)

    database.commit()


# Provide the connection to the database to all other scripts

def db_connection():
    return database


if __name__ == "__main__":
    database_setup()
