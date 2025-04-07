# Building a Secure Login System
This project demonstrates how to build a secure login system using Python, SQLite, and bcrypt for password hashing.
It consists of three main scripts to handle database creation, user management, and client login functionality.

## Steps to follow:
### Create the Database
Start by running the server-side script that initializes the database.
📄 Check out: Create_DB.py

### Client-Side: Login & Signup GUI
Run the client script that provides a user-friendly GUI for logging in or signing up.

- The client sends login/signup requests to the server.

- The server checks the database for valid credentials.

- Passwords are securely hashed using bcrypt.

- If the user doesn't exist, they can create a new account via the signup page.

📄 Check out: main.py

### Database Manager Console Tool
For administrative tasks, use the database manager script to:

- Add multiple users manually (with hashed passwords).

- View all records in the database.

- Delete specific users if needed.

All operations are performed via the console.

📄 Check out: Db_manager.py

## Recommended Order of Execution:
To see the complete flow of the application, follow these steps:

1. Run Create_DB.py — This will create the SQLite database with the required schema.

2. Run main.py — Use the signup page to add some sample users.

3. Optionally, run Db_manager.py — Add multiple users at once, view all users, or delete specific users from the console.

4. Test the Login System!

  - Try logging in with valid user credentials.

  - Try logging in with a username that doesn't exist to see how the system responds.
