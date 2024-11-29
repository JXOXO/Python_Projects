from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

#So when we go to the txt file we can see the password, so we will encrypt them
#Define a key
#So it is going to take a string of text and using a key turned to a completely to a random string of text
#that we can't get back to the original text without knowing the key
#I will combine the key with User_pwd and use this to encrypt the text
#then if user type the wrong password = decrypt the text and get something that make no sense 
#so you need the key and password to get to the original text

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt

#we need two function
#   1) that create the key
#   2) that that can retrieve a key

#function that creates the key
def write_key():
    salt = os.urandom(16)  # Generate a random 16-byte salt
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
# Function to load the salt
def load_salt():
    try:
        with open("key.key", "rb") as key_file:
            salt = key_file.read()
        return salt
    except FileNotFoundError:
        print("Salt file not found! Did you run write_key() to create it?")
        exit(1)

# Derive the encryption key using the user's password and the saved salt
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Load the saved salt
salt = load_salt()

user_pwd = input("What is your password? ") # Prompt the user for their password and derive the encryption key
key = derive_key(user_pwd, salt)  # Derive a consistent encryption key
fer = Fernet(key)  # Create a Fernet object for encryption and decryption
        
# Functions for viewing passwords
def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                try:
                    data = line.rstrip()    #rstrip() remove the return new line so when view the content in terminal it will not show the line separated by a break line
                    user, passw = data.split("|")   #This will find this char ("|") and all strings that are separated by "|" and return them in a list, use index to access the strings
                    decrypted_password = fer.decrypt(passw.encode()).decode()   # Decrypt the password
                    print(f"User: {user} | Password: {decrypted_password}")
                except Exception as e:
                    print(f"Error during decryption for line '{line.strip()}': {e}")
    except FileNotFoundError:
        print("No passwords saved yet.")
    except Exception as e:
        print(f"Error reading file: {e}")
            
#Create a file if the file that stores the passwords does not exist, and add the password into it
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    #(with) help when user done with all the files, it will automatically close the file
    #Modes to open the file in:
    #   1) a -> means pend mode, allow us to add something to the end of an existing file and create new file if that file doesn't exist
    #   2) w -> means write, it creates or override the file if it exists 
    #   3) r -> means read, only read mode, can't write anything to the file 
    with open("passwords.txt", "a") as f:
        encrypted_password = fer.encrypt(pwd.encode()).decode()  # Encrypt the password
        f.write(f"{name} | {encrypted_password}\n")  # Save it in the file


while True:
    mode = input("Would like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue