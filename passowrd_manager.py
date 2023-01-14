import sys
from database_manager import addToDB, viewFromDB, masterStore, masterRetrieve 
from encryption import hashMaster
import os

def addLogin():
    username = input("Username: ")
    password = input("Password: ")
    addToDB(username,password)

def viewLogins():
    ans = viewFromDB()
    for tup in ans:
        print(tup[0], tup[1], sep="\n")

def firstRun():
    if os.path.exists("sql.db") == False:
        sys.stdout.write("No creds-locker database found!!\n")
        num = int(input("Press 1, if you are New user\nPress 2, to exit\n"))
        if num==1:
            password = input("Enter new master passowrd: ")
            encryptedPass = hashMaster(password)
            masterStore(encryptedPass)
        elif num==2:
            sys.stdout.write("Exit the program")
            sys.exit()

def checkMasterPass():
    password = input("Enter the master passowrd:- ")
    encryptedPass = hashMaster(password)
    correcthash = masterRetrieve()
    if encryptedPass==correcthash.lower():
        return True
    return False
    
if __name__=="__main__":
    firstRun()
    isCorrect = checkMasterPass()
    if isCorrect:
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
