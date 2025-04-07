# This script provides a simple command-line interface ebaleling the Database manager to view, add and delete records from a SQLite database.
# It connects to a SQLite database named "users.db" and allows the Database Manager to view all records or delete a specific record by username.

import sqlite3 # Importing SQLite3 for database operations
import bcrypt # Importing bcrypt for password hashing
import os # Importing os for file path operations
1
DB_FILE = "users.db" # Database file name

# Initialize the database (only if it doesn't exist)
def initialize_database(): # This function initializes the database and creates the users table if it doesn't exist.
    if not os.path.exists(DB_FILE): # Check if the database file exists
        conn = sqlite3.connect(DB_FILE) # Connect to the database (or create it if it doesn't exist)
        cursor = conn.cursor() # Create a cursor object for executing SQL commands
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                fullname TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """) # Create a table named users with the specified columns and constraints
        
        conn.commit() # Commit the changes to the database
        conn.close() # Close the connection to the database
        print("Database initialized successfully.") # Print a message indicating that the database has been initialized successfully.
    else:
        print("Database already exists. Ready to manage users.") # Print a message indicating that the database already exists and is ready for use.

# Function to add new users
def add_user(): 
    try:
        conn = sqlite3.connect(DB_FILE) # Connect to the database
        cursor = conn.cursor() # Create a cursor object for executing SQL commands

        while True: # Loop to allow adding multiple users
            username = input("Enter a new username (or type 'done' to finish): ").strip() # Prompt for username .strip() removes leading and trailing whitespace.
            if username.lower() == 'done': # Check if the Database Manager wants to finish adding users
                break

            # Check if username already exists
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,)) # Execute SQL command to check if the username already exists in the database
            if cursor.fetchone(): # If the username exists, fetchone() will return a tuple with the username, otherwise it will return None
                print("This username already exists. Please choose another.") # Print a message indicating that the username already exists
                continue

            password = input("Enter password for the user: ").strip() # Prompt for password .strip() removes leading and trailing whitespace.
            fullname = input("Enter full name: ").strip() # Prompt for full name .strip() removes leading and trailing whitespace.
            email = input("Enter email address: ").strip() # Prompt for email address .strip() removes leading and trailing whitespace.
            phone = input("Enter phone number: ").strip() # Prompt for phone number .strip() removes leading and trailing whitespace.

            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) # Hash the password using bcrypt

            # Insert into database
            cursor.execute("""
                INSERT INTO users (username, password, fullname, email, phone)
                VALUES (?, ?, ?, ?, ?)
            """, (username, hashed_password.decode('utf-8'), fullname, email, phone)) # Execute SQL command to insert the new user into the database
            conn.commit() # Commit the changes to the database

            print(f"User '{username}' has been added successfully!\n") # Print a message indicating that the user has been added successfully

        conn.close() # Close the connection to the database

    except Exception as e:
        print("An error occurred while adding user:", e) # Print an error message if an exception occurs

# Function to view all records
def view_records(): 
    conn = sqlite3.connect(DB_FILE) # Connect to the database
    cursor = conn.cursor() # Create a cursor object for executing SQL commands
    
    cursor.execute("SELECT username, fullname, email, phone FROM users") # Execute SQL command to select all records from the users table
    users = cursor.fetchall() # Fetch all records from the result set
    
    print("\nAll Users in Database:") # Print a header for the user list
    for user in users:
        username, fullname, email, phone = user
        print(f"Username: {username}, Full Name: {fullname}, Email: {email}, Phone: {phone}") # Print each user's details
    
    conn.close() # Close the connection to the database

# Function to delete a specific record by username
def delete_record():
    try:
        username = input("Enter the username of the user to delete: ").strip() # Prompt for username .strip() removes leading and trailing whitespace.
        conn = sqlite3.connect(DB_FILE) # Connect to the database
        cursor = conn.cursor()  # Create a cursor object for executing SQL commands
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,)) # Execute SQL command to check if the username exists in the database
        record = cursor.fetchone() # Fetch the record with the specified username
        
        if record:
            cursor.execute("DELETE FROM users WHERE username = ?", (username,)) # Execute SQL command to delete the record with the specified username
            conn.commit() # Commit the changes to the database
            print(f"Record with username '{username}' has been deleted.") # Print a message indicating that the record has been deleted
        else:
            print(f"No record found with username '{username}'.")   # Print a message indicating that no record was found with the specified username
            
        conn.close()  # Close the connection to the database
        
    except Exception as e:
        print("An error occurred:", e) # Print an error message if an exception occurs

# Main menu
def main():
    initialize_database() # Initialize the database if it doesn't exist

    while True: # Loop to display the main menu
        print("\nDatabase Manager Options:")
        print("1. Add new user(s)")
        print("2. View all records")
        print("3. Delete a specific record")
        print("4. Exit")
        
        choice = input("Select an option (1, 2, 3, or 4): ").strip() # Prompt for user choice .strip() removes leading and trailing whitespace.
        # Validate user input
        if choice == '1':
            add_user()
        elif choice == '2':
            view_records()
        elif choice == '3':
            delete_record()
        elif choice == '4':
            print("Exiting Database Manager.")
            break
        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
