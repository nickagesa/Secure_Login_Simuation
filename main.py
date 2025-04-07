# This is a simple login and sign-up application using Tkinter for GUI and SQLite3 for database operations.
# It allows users to create an account and log in with their credentials. Passwords are hashed using bcrypt for security.
# The application consists of two main classes: LoginScreen and SignUpScreen, each handling its respective functionality.
# Install the required libraries using the following command:
# pip install bcrypt tkinter sqlite3

# Importing necessary libraries
import sqlite3 # Importing SQLite3 for database operations
import tkinter as tk # Importing Tkinter for GUI
from tkinter import messagebox # Importing messagebox for pop-up messages
import bcrypt # Importing bcrypt for password hashing

# Function to hash passwords
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode('utf-8')


# Function to check if a username already exists
def username_exists(username):
    conn = sqlite3.connect("users.db") # Connect to the database
    cursor = conn.cursor() # Create a cursor object for executing SQL commands
    cursor.execute("SELECT username FROM users WHERE username=?", (username,)) # Check if the username exists
    exists = cursor.fetchone() # Fetch the result
    # If the username exists, fetchone() will return a tuple with the username, otherwise it will return None
    conn.close() # Close the connection
    return exists is not None # Return True if the username exists, otherwise return False

# Login Page Class
class LoginScreen:
    def __init__(self, root): # Initialize the LoginScreen class
        self.root = root # Create a root window
        self.root.title("Login") # Set the title of the window
        self.root.geometry("300x250") # Set the size of the window
        self.root.resizable(False, False) # Make the window non-resizable

        # Username
        self.username_label = tk.Label(root, text="Username:") # Create a label for username
        self.username_label.pack() # Pack the label into the window
        self.username_entry = tk.Entry(root) # Create an entry field for username
        self.username_entry.pack() # Pack the entry field into the window

        # Password
        self.password_label = tk.Label(root, text="Password:") # Create a label for password
        self.password_label.pack() # Pack the label into the window
        self.password_entry = tk.Entry(root, show="*") # Create an entry field for password with asterisks
        self.password_entry.pack() # Pack the entry field into the window

        # Login Button
        self.login_button = tk.Button(root, text="Login", command=self.login) # Create a button for login
        self.login_button.pack() # Pack the button into the window

        # Sign Up Button
        self.signup_button = tk.Button(root, text="Sign Up", command=self.go_to_signup) # Create a button for sign up
        self.signup_button.pack() # Pack the button into the window

    # Login function
    def login(self): # Define the login function
        username = self.username_entry.get() # Get the username from the entry field
        password = self.password_entry.get() # Get the password from the entry field

        conn = sqlite3.connect("users.db") # Connect to the database
        cursor = conn.cursor() # Create a cursor object for executing SQL commands

        # Fetch user from database
        cursor.execute("SELECT password FROM users WHERE username=?", (username,)) # Execute SQL command to fetch the password for the given username
        user = cursor.fetchone() # Fetch the result
        # If the username exists, fetchone() will return a tuple with the password, otherwise it will return None

        conn.close() # Close the connection

        # Check if user exists and verify password
        if user and bcrypt.checkpw(password.encode(), user[0].encode('utf-8')): # If the user exists and the password matches
            # Successful login
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showerror("Error", "Invalid username or password") # Show error message if login fails

    # Switch to Sign-Up Page
    def go_to_signup(self): # Define the function to switch to sign-up page
        self.root.destroy() # Destroy the current window
        root = tk.Tk() # Create a new root window
        SignUpScreen(root) # Create an instance of SignUpScreen class
        root.mainloop() # Run the application


# Sign-Up Page Class
class SignUpScreen:
    def __init__(self, root): # Initialize the SignUpScreen class
        self.root = root # Create a root window
        self.root.title("Sign Up") # Set the title of the window
        self.root.geometry("300x350") # Set the size of the window
        self.root.resizable(False, False) # Make the window non-resizable

        # Full Name
        self.fullname_label = tk.Label(root, text="Full Name:") # Create a label for full name
        self.fullname_label.pack() # Pack the label into the window
        self.fullname_entry = tk.Entry(root) # Create an entry field for full name
        self.fullname_entry.pack() # Pack the entry field into the window

        # Email
        self.email_label = tk.Label(root, text="Email:") # Create a label for email
        self.email_label.pack() # Pack the label into the window
        self.email_entry = tk.Entry(root) # Create an entry field for email
        self.email_entry.pack() # Pack the entry field into the window

        # Phone Number
        self.phone_label = tk.Label(root, text="Phone:") # Create a label for phone number
        self.phone_label.pack() # Pack the label into the window
        self.phone_entry = tk.Entry(root) # Create an entry field for phone number
        self.phone_entry.pack() # Pack the entry field into the window

        # Username
        self.username_label = tk.Label(root, text="Username:") # Create a label for username
        self.username_label.pack() # Pack the label into the window
        self.username_entry = tk.Entry(root)  # Create an entry field for username
        self.username_entry.pack()  # Pack the entry field into the window

        # Password
        self.password_label = tk.Label(root, text="Password:")  # Create a label for password
        self.password_label.pack() # Pack the label into the window
        self.password_entry = tk.Entry(root, show="*") # Create an entry field for password with asterisks
        self.password_entry.pack() # Pack the entry field into the window

        # Sign Up Button
        self.signup_button = tk.Button(root, text="Sign Up", command=self.signup) # Create a button for sign up
        self.signup_button.pack()   # Pack the button into the window

        # Back to Login Button
        self.back_button = tk.Button(root, text="Back to Login", command=self.go_to_login) # Create a button to go back to login
        self.back_button.pack() # Pack the button into the window

    # Sign-Up Function
    def signup(self): # Define the sign-up function
        # Get user input
        fullname = self.fullname_entry.get() # Get the full name from the entry field
        email = self.email_entry.get()  # Get the email from the entry field
        phone = self.phone_entry.get() # Get the phone number from the entry field
        username = self.username_entry.get() # Get the username from the entry field
        password = self.password_entry.get()    

        # Validate fields
        if not all([fullname, email, phone, username, password]): # Check if all fields are filled
            messagebox.showerror("Error", "All fields are required")   # Show error message if any field is empty
            return 

        # Check if username already exists
        if username_exists(username): # Check if the username already exists in the database
            messagebox.showerror("Error", "Username not available") # Show error message if username is taken
            return

        # Hash the password
        hashed_password = hash_password(password) # Hash the password using bcrypt

        # Insert into database
        conn = sqlite3.connect("users.db") # Connect to the database
        cursor = conn.cursor() # Create a cursor object for executing SQL commands
        cursor.execute("INSERT INTO users (username, password, fullname, email, phone) VALUES (?, ?, ?, ?, ?)",
                       (username, hashed_password, fullname, email, phone)) # Execute SQL command to insert user data into the database
        conn.commit() # Commit the changes to the database
        conn.close() # Close the connection

        messagebox.showinfo("Success", "Account created successfully!") # Show success message
        self.go_to_login() # Switch to Login Page

    # Switch to Login Page
    def go_to_login(self): # Define the function to switch to login page
        self.root.destroy() # Destroy the current window
        root = tk.Tk() # Create a new root window
        LoginScreen(root) # Create an instance of LoginScreen class
        root.mainloop() # Run the application


# Run the application
if __name__ == "__main__": # Check if the script is being run directly
    root = tk.Tk() # Create a root window
    LoginScreen(root) # Create an instance of LoginScreen class
    root.mainloop() # Run the application