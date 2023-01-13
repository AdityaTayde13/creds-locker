import sys

un_pass_dict = {}

def addLogin():
    username = input("Username: ")
    password = input("Password: ")
    un_pass_dict[username] = password

def viewLogins():
    sys.stdout.write("| username | password ")
    for k, v in un_pass_dict.items():
        sys.stdout.write(" | %s  | %s \n" % (k, v))

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
