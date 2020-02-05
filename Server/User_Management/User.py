from Database import UserDB

# Opens existing database
database = UserDB("user_info.db")

# Creates User
def create_user():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    email = input("Enter email: ")
    avail = database.checkAvail(email)

    # Email not valid
    while avail == 0 or "@gmail.com" not in email:
        print("Invalid email. Either user already exists or email address not supported \n(ei, valid:someone@gmail.com)")
        email = input("\n\nEnter a valid email address: ")
        avail = database.checkAvail(email)

    password = input("Enter new password: ")
    password2 = input("Confirm password: ")

    # Password not valid
    while password != password2:
        print("Passwords do not match\n\n")
        password = input("Enter new password: ")
        password2 = input("Confirm password: ")

    database.insert(email, password, fname, lname)

# Login for user
def login():
    email = input("Enter username/email: ")
    avail = database.checkAvail(email)

    real_password = 0

    if avail == 0:
        real_password = database.fetch_userPASS(email)[0][0]

    entered_password = input("Enter password: ")

    # Username or password are invalid
    while entered_password != real_password or avail == 1 or "@gmail.com" not in email:
        print("Invalid username or password.  Try again.")
        email = input("\nEnter username/email: ")
        avail = database.checkAvail(email)

        real_password = database.fetch_userPASS(email)
        entered_password = input("Enter password: ")


request = input("[1] Create New User or [2] Login: ")

if request == '1':
    create_user()

elif request == '2':
    login()

else:
    print("Wrong input")

database.exit()
