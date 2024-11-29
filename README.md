# Python_Projects
Working on improving Python skills 🚀

---

# Project 1
## Password Manager 🔐

This Python-based **Password Manager** securely stores and manages your account credentials using **encryption**. The program encrypts passwords to ensure that stored data remains inaccessible without the correct master password. This makes it a practical solution for managing sensitive information while ensuring data security.

---

## Features

- **Secure Password Encryption**: Uses the `cryptography` library's Fernet symmetric encryption.
- **Salt-Based Key Derivation**: Derives a unique encryption key from your master password and a stored random salt.
- **Password Management**:
  - **Add**: Save account names and passwords securely.
  - **View**: Retrieve and decrypt stored passwords using the correct master password.
- **Master Password Validation**: Ensures only users with the correct password can access stored credentials.
- **Persistent Storage**: Stores encrypted passwords in a `passwords.txt` file, protected from unauthorized access.

---

## How It Works

1. **Key Creation**: A unique salt is generated (`key.key`) and stored. This salt, combined with your master password, derives the encryption key.
2. **Encryption**: When adding a new password, it is encrypted using the derived key and stored in `passwords.txt`.
3. **Decryption**: When viewing passwords, the program uses the same key derived from the master password to decrypt and display the data.
4. **Access Control**: Without the correct master password, decryption is impossible, ensuring security.

---

### Requirements

- Python 3.6 or later
- `cryptography` library

Install the required library:
pip install cryptography

---

## Usage

1. **Initialize the Program**: Run the script and set up the salt file:
    - python3 PasswordManager.py
    - If the key.key file does not exist, run the write_key() function to generate it.
2. **Enter Master Password**: On each run, the program prompts you for your master password. This is used to derive the encryption key for the session.
3. **Add or View Passwords**: When viewing passwords, the program uses the same key derived from the master password to decrypt and display the data.
    - Add a New Password: Enter an account name and a password to securely store.
    - View Existing Passwords: Retrieve and decrypt stored credentials.
4. **Exit**: Enter q to quit the program.

---

## File Structure
  - key.key: Stores the random salt used for deriving the encryption key.
  - passwords.txt: Stores account names and encrypted passwords.

---

## Security Notes

1. **Consistency is Key**: Always use the same master password to ensure the encryption key remains consistent.
2. **Salt Safety**: Keep the key.key file secure. If lost, stored passwords cannot be decrypted.
3. **Encryption Strength**: The program uses AES encryption with a 32-byte key derived using PBKDF2-HMAC with SHA256 hashing.

---

## Future Enhancements

1. **Password Strength Validation**: Check the strength of passwords before saving.
2. **Password Generation**: Automatically generate strong passwords for users.
3. **GUI Support**: Add a graphical user interface for easier interaction.

---
