import os
from getpass import getpass


if not os.path.exists('database.txt'):
    fh = open('database.txt','w')
    fh.close()


def register():
    username=input("Enter username:  ")
    if username in open('database.txt','r').read():
        print("Username already exits")
        exit()
    password = getpass("Enter password")
    c_password = getpass("enter conform password")
    if password != c_password:
        print("pass not match")
        exit()

    handle = open('database.txt','a')
    handle.write(username)
    handle.write("")
    handle.write(password)
    handle.write("\n")
    handle.close()
    print("User was successful register")
    exit()









def login():
    username = input("Enter username:")
    password = getpass("Enter password:")
    get_record = open('database.txt','r').readlines()
    users = []
    for user in get_record:
      users.append(user.split())


    total_users = len(users)
    inc = 0
    login_success = False
    while inc < total_users:
        uname = users[inc][0]
        pas = users[inc][1]
        if username ==uname and password ==pas:
            login_success = True

        inc +=1
    if login_success == True:
        print(f"welcome{username}")
    else:
        print("username and pasword donot match")

question = input("Do you have an account y/n")

if question == 'y':
    login()
else:
    register()


def update():
    fl = open('database.txt','r')
    errr=input("do you want to update")