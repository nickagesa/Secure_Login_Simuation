# This script creates a SQLite database named "users.db" and a table named "users" within that database.
# The table has five columns: username, password, fullname, email, and phone.
# The username is the primary key, meaning it must be unique for each user.
# The password, fullname, email, and phone columns cannot be NULL, meaning they must always have a value.
# The script also commits the changes to the database and closes the connection.

# Import the necessary libraries
import sqlite3 # Import the SQLite library to interact with SQLite databases


conn = sqlite3.connect("users.db") # Connect to the database, If the file does not exist, SQLite will create it.
cursor = conn.cursor() # Create a cursor object that allows you to interact with the database.

# The cursor acts like a middleman between your Python program and the database, 
# enabling you to execute SQL queries (e.g., SELECT, INSERT, UPDATE, DELETE).

# create a users table in the database
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT Primary Key,
    password TEXT not null,
    fullname TEXT not null,
    email TEXT not null,
    phone TEXT not null
)""") # Create a table in the database

# CREATE TABLE IF IT NOT EXISTS users → This creates a table named users if it does not already exist.
# username TEXT PRIMARY KEY → The username column is of type TEXT and is the primary key (it must be unique).
# password TEXT NOT NULL → The password column is also of type TEXT and cannot be NULL (it must always have a value).

# Commit and close connection
conn.commit() # Commit the changes to the database. This saves all the changes made to the database.
# If you don't call this method, the changes will not be saved to the database.
conn.close() # Close the connection to the database. This is important to free up resources and avoid potential data corruption.
# Closing the connection is a good practice after you are done with database operations.

