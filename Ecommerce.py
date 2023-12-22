# (Intermmediate) Task : Ecommerce application
# Requirements
# - Ask user login or register
# - If regiser ask if he/she is buyer or seller
# - While login if user is buyer, give him choices : 1. View ,2. Buy 3. View bills
# - If user is seller, give him choices, give him/her : 1. Add products, View his/her products, 3. View his/her billed products.

import json

# Register User Function
def register():
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    user_type = input('Enter your user type :Buyer or Seller ').lower()

    user_data = {'username':username,'password':password, 'user_type':user_type}
    json_user_data = json.dumps(user_data)
    f = open('user_db.txt','a')
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
                user_user_type = user_dict_data.get('user_type')

    if login ==True:
        print('Login successful.')
        if user_user_type == 'buyer':
            print('''
                    1. View all products
                    2. View all your bills
                  ''')
            user_choice = input('Enter a choice : ')
            if user_choice == '1':
                view_products(username)
            elif user_choice == '2':
                view_bills(username)
        else:
            print('''
                    1. Add product
                    2. View all products
                    3. View all bills
                  ''')
            user_choice = input('Enter a choice : ')
            if user_choice == '1':
                add_product(username)
            elif user_choice == '2':
                view_seller_products(username)
            elif user_choice == '3':
                view_bills(username)

    else:
        print('Invalid Login.')

# Buyer View Products Function
def view_products(buyer):
    f = open('products.txt','r')

    content = f.read()

    list_product_data = content.split('-')

    for i in list_product_data:
        print(i)

    user_purchase_product_name = input('Enter the product name you want to purchase : ').lower()
    user_purchase_product_quantity = int(input('Enter the quantity you want to purchase : '))

    for i in list_product_data:
        if i != '':
            product_dict_data = json.loads(i)
            if product_dict_data.get('product_name') == user_purchase_product_name:
                product_data = product_dict_data
                product_price = product_dict_data.get('product_price')
                int_product_price = int(product_price)

    total = user_purchase_product_quantity * int_product_price

    print(f'Your total is : {total}')

    purchase_product_dict_data = {"product_name":product_data.get('name'),"product_price":product_data.get('price'),"quantity":user_purchase_product_quantity,"total":total,"seller":product_data.get('seller'),"buyer":buyer}
    json_product_data = json.dumps(purchase_product_dict_data)

    f = open('bill.txt','a')
    f.write(json_product_data + '-')
    f.close()

#Buyer View Bills function
def view_bills(username):
    f = open('bill.txt','r')
    content = f.read()
    f.close()

    list_bill_data = content.split('-')

    for i in list_bill_data:
        if i != '':
            bill_dict_data = json.loads(i)
            if bill_dict_data.get('buyer') == username:
                print(i)

# Add Product by seller
def add_product(seller):
    product_name = input('Enter Product name : ')
    product_price = input('Price of Product : ')
    product_description = input('Enter Product Description ')

    product_data = {'product_name':product_name, 'product_price':product_price, 'product_description':product_description, 'seller':seller}
    json_user_data = json.dumps(product_data)
    f = open('products.txt','a')
    f.write(json_user_data + '-')
    f.close()
    print('Product Added successfully!')

# Seller View Products Function
def view_seller_products(seller):
    f = open('products.txt', 'r')
    content = f.read()
    f.close()

    list_product_data = content.split('-')

    for i in list_product_data:
        if i != '':
            product_dict_data = json.loads(i)
            if product_dict_data.get('seller') == seller:
                print(i)

#Seller View Bills Function
def view_seller_bills(seller):
    f = open('bill.txt', 'r')
    content = f.read()
    f.close()

    list_bill_data = content.split('-')

    for i in list_bill_data:
        if i != '':
            bill_dict_data = json.loads(i)
            if bill_dict_data.get('seller') == seller:
                print(i)


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