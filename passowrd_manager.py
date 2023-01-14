import sys
from database_manager import addToDB
from database_manager import viewFromDB


def addLogin():
    username = input("Username: ")
    password = input("Password: ")
    addToDB(username,password)

def viewLogins():
    ans = viewFromDB()
    for tup in ans:
        print(tup[0], tup[1], sep="\n")

password = input("Enter the master passowrd:- ")
if password == "abcd":
    while True:
        options = input("\nEnter \"A\" to add login\n Enter \"V\" to view the login\n Enter \"q\" to quit the password manager\n:").lower()
        if options=='a':
            addLogin()
        elif options=='v':
            viewLogins()
        elif options=='q':
            break
        else:
            sys.stderr.write("Invalid option, Please Try Again!!")
else:
    sys.stderr.write("Wrong master password, Exiting the Program\n")
    sys.exit(1)
