# Requirements
# Ask user for login or register
# 1. View Total Amount
# 2. Deposit amount
# 3. Withdraw amount
# 4. Exit
import json

def register():
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    user_data = {'username':username,'password':password}
    json_user_data = json.dumps(user_data)
    f = open('ecommerceuser_db.txt','a')
    f.write(json_user_data + '-')
    f.close()
    print('Account created successfully!')

# User login Function
def login():
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    f = open('user_db.txt','r')
    content = f.read()
    f.close()
    list_data = content.split('-')
    login = False
    user_user_type = None
    for i in list_data:
        if i != '':
            user_dict_data = json.loads(i)
            if username == user_dict_data.get('username') and password == user_dict_data.get('password'):
                login = True

    if login ==True:
        print('Login successful.')
        print('''
                    1. View Total Amount
                    2. Deposit amount
                    3. Withdraw amounts
                  ''')
        user_choice = input('Enter a choice : ')
        if user_choice == '1':
            view_amount(username)
        elif user_choice == '2':
            deposit_amount(username)
        elif user_choice == '3':
            withdraw_amount(username)

    else:
        print('Invalid Login.')


def deposit_amount(account_name):
    deposit_amount = input('Enter The Amount You Want To Deposit : ')
    account_data = {'deposit_amount':deposit_amount, 'account_name':account_name}
    json_account_data = json.dumps(account_data)
    f = open('account_db.txt','a')
    f.write(json_account_data + '-')
    f.close()
    print('Amount Added successfully!')


def view_amount(username):
        f = open('account_db.txt', 'r')
        content = f.read()
        f.close()

        list_amount = content.split('-')

        for i in list_amount:
            if i != '':
                view_dict_data = json.loads(i)
                if view_dict_data.get('account_name') == username:
                    print("Account Name : ", view_dict_data.get('account_name'))
                    print("Total Amount : ", view_dict_data.get('deposit_amount'))


def withdraw_amount(username):
    amount = float(input("Enter the amount to withdraw: "))
    try:
        with open('account_db.txt', 'r') as f:
            content = f.read()
            list_account_data = content.split('-')
            for i in list_account_data:
                if i != '':
                    account_dict_data = json.loads(i)
                    if account_dict_data.get('account_name') == username:
                        balance = float(account_dict_data.get('deposit_amount'))

                        if balance >= amount:
                            balance_amount = balance - amount
                            account_dict_data['deposit_amount'] = str(balance_amount)
                            json_user_data = json.dumps(account_dict_data)

                            with open('account_db.txt', 'w') as f:
                                f.write(json_user_data)

                            print(f"Withdrew {amount} from the account. New balance is {balance_amount}.")
                        else:
                            print("Insufficient balance to withdraw.")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid balance value in the file.")


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
            register()
        elif user_input == 2:
            login()
        elif user_input == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
# main constructor
if __name__ == "__main__":
    main()