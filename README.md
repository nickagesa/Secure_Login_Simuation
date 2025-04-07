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
  
#  Future Improvements
Here are some ideas to further enhance the project:

- Password Reset Functionality - Add an option for users to reset their password via email verification or security questions.
- Email Verification on Signup -Send a verification link to the user's email to confirm their account before activation.
- Role-Based Access Control (RBAC) - Implement roles such as Admin, User, or Guest to restrict or allow access to certain features.
- Activity Logging - Track login attempts, successful and failed, for better audit and security monitoring.
- Two-Factor Authentication (2FA) - Enhance security by requiring a second form of verification during login.
- Improved UI/UX - Upgrade the GUI to a modern, sleek design with better user interaction and feedback.
- Deployment as a Web Application - Consider deploying this system as a web-based platform using Flask or Django.
- Dockerization - Containerize the application for easier deployment and scaling.
- Automated Testing - Add unit tests and integration tests to ensure code reliability.

  

