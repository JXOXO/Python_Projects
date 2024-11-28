User_pwd = input("What is your password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line)

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
        f.write(name + " | " + pwd + "\n")


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