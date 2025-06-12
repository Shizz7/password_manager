# password_manager

Password Manager

This is a simple and effective password manager built with Python. It features an easy-to-use graphical interface using Tkinter and allows users to securely manage their website credentials. You can add, search, edit, and even generate strong passwords, all of which are stored locally in a JSON file.

Key Features
1. Clean and interactive user interface built with Tkinter

2. Add new login credentials (website, email/username, password)

3. Search for saved entries by website name

4. Edit existing credentials directly from the interface

5. Generate strong, random passwords

6. Copy generated passwords to the clipboard (optional)

7. Data is saved in a local JSON file for easy access and persistence

8. Validates user input to prevent incomplete entries

9. Gracefully handles missing or corrupt files and unexpected errors

Technologies Used
1. Python 3

2. Tkinter for building the GUI

3. JSON for data storage

4. Random and string libraries for password generation

5. Pyperclip for copying passwords to clipboard

How to Use

Run the application.

Enter the website, email/username, and password.

You can click the "Generate Password" button to auto-create a strong password.

Click "Add" to save the information.

Use the "Search" feature to retrieve saved credentials.

You can also edit any existing entry if needed.

All saved data is stored in a data.json file located in the same directory as the script.

Input Validation and Error Handling

If any input field is left empty, the program will prompt the user to fill it.

If the data file is missing, it is automatically created.

If a website is not found during a search, an appropriate message is displayed.

Errors related to file access or invalid operations are handled gracefully to avoid crashes.
