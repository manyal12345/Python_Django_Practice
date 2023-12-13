# Requirements
# Keep the program on infinite loop so that the data stored on list will not be erased
# Give the user three choices login, register, and exit
# If login check, the username and password provided by user in user_db list
# Else if register, add the username and password in the user_db list
# Else if exit, exit the program by ending the infinite loop

import json

def register(username, password):
    user_data = {'username':username,'password':password}
    json_user_data = json.dumps(user_data)
    f = open('user_db.txt','a')
    f.write(json_user_data + '-')
    f.close()
    print('Account created successfully!')

def login(username,password):
    f = open('user_db.txt','r')
    content = f.read()
    f.close()
    list_data = content.split('-')
    login = False
    for i in list_data:
        if i != '':
            user_dict_data = json.loads(i)
            if username == user_dict_data.get('username') and password == user_dict_data.get('password'):
                login = True

    if login == True:
        print('Login successfull!')
    else:
        print('Invalid login!')


def main():
    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        user_in = input("Enter your choice: ")
        try:
            user_input = int(user_in)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if user_input == 1:
            user_username = input('Enter your username : ')
            user_password = input('Enter your password : ')
            register(user_username, user_password)
        elif user_input == 2:
            user_username = input('Enter your username : ')
            user_password = input('Enter your password : ')
            login(user_username, user_password)
        elif user_input == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
# main constructor
if __name__ == "__main__":
    main()