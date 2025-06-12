

---

Secure Password Manager

This is a simple yet secure desktop password manager application, built using Python and Tkinter. It helps you safely store and manage your website credentials locally on your computer.

 Features
**Master Password Protection**: All your stored passwords are encrypted and protected by a single master password that you set.
**Strong Encryption**: Uses `cryptography.fernet` for robust encryption of your sensitive data.
**Password Generation**: Generate strong, random passwords with a mix of letters, numbers, and symbols.
**Easy Management**: Add, search for, and edit your stored website credentials.
**Local Storage**: Your data is stored securely on your own device, not on any external servers.

---

## How to Use

Since this project is provided as an executable file, you don't need to install Python or any libraries to run it.

1.  **Download the Executable**:
    * Locate the executable file (e.g., `PasswordManager.exe` on Windows, or the corresponding executable for macOS/Linux) provided in the project distribution.

2.  **Run the Application**:
    * **Windows**: Double-click the `PasswordManager.exe` file.
    * **macOS/Linux**: You might need to make the file executable first:
        ```bash
        chmod +x PasswordManager
        ./PasswordManager
        ```

3.  **Set Your Master Password (First-time Use)**:
    * The first time you run the application, a small window will appear prompting you to **Set Master Password**.
    * **Choose a strong, memorable master password.** This password will be the *only* way to access your stored credentials. If you forget it, your data will be inaccessible.
    * Enter your master password and click "Set".

4.  **Log In (Subsequent Uses)**:
    * After setting your master password, or on any subsequent run, a window will appear asking you to **Enter Master Password**.
    * Enter the master password you previously set to unlock the application.

5.  **Using the Password Manager**:

    * **Website**: Enter the name of the website (e.g., "Google", "Facebook").
    * **Email/Username**: Enter the email address or username associated with that website.
    * **Password**:
        * You can manually type a password.
        * Click **"Generate Password"** to create a strong, random password. The generated password will automatically be copied to your clipboard.
    * **"Add" Button**: Saves the website, email/username, and password to your secure storage.
    * **"Search" Button**: Enter a website name in the "Website" field and click "Search" to retrieve the stored email/username and password for that site.
    * **"Edit" Button**: Enter the website, and the new email/username and password you want to update. Click "Edit" to save the changes.

---

## Important Notes

* **Remember Your Master Password**: This is crucial! There is no recovery mechanism if you forget your master password, and your encrypted data will become inaccessible.
* **Security**: While this manager provides local encryption, always practice good security hygiene. Keep your executable file in a secure location and ensure your operating system is protected.
* **Data Files**: The application creates a few files in the same directory as the executable:
    * `master.hash`: Stores the hashed version of your master password (for verification).
    * `key.key`: Stores the encryption key used to encrypt your data.
    * `data.json`: Stores your encrypted website credentials.
    **Do not delete these files**, as doing so will result in data loss or an inability to access your passwords.

---
