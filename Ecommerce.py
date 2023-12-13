# (Intermmediate) Task : Ecommerce application with two users buyer and seller seller can add product and
# view there products buyer can view all products from different sellers and can purchase one product,
# after purchase a bill listing total amount for buyer should be printed out

# Global variables to store product information
products = []



# Add product
def add_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    seller_name = input("Enter seller name: ")

# define product dictionary
    product = {
        "name": product_name,
        "price": price,
        "seller": seller_name
    }

    products.append(product)
    print("Product added successfully!")
# View Products seller wise
def view_products(seller_name):
    print("\nYour Products:")
    for product in products:
        if product["seller"] == seller_name:
            print(f"Product: {product['name']}, Price: Rs.{product['price']}")

# View All Products from products dictionary
def view_all_products():
    print("\nAll Products:")
    for product in products:
        print(f"Product: {product['name']}, Price: Rs. {product['price']}, Seller: {product['seller']}")

    #buyer to purchase a product
    purchase = input("Do you wanna purchase a product? (y/n): ")
    if purchase.lower() == "y":

        product_index = int(input("Enter the index of the product you want to purchase: "))

        if 0 <= product_index < len(products):
            selected_product = products[product_index]

            total_amount = product['price']

            print("\nBill:")
            for product in products:
                print(f"Product: {product['name']}, Price: Rs.{product['price']}")

            print(f"Total Amount: Rs.{total_amount}")
        else:
            print("Invalid product index.")
    else:
        print("Returning to main menu.")


# Main Ecommerce Program
def main():
    while True:
        print("1. Seller: Add Product")
        print("2. Seller: View Products")
        print("3. Buyer: View All Products")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_product()
        elif choice == 2:
            seller_name = input("Enter your name as a seller: ")
            view_products(seller_name)
        elif choice == 3:
            view_all_products()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
# main constructor
if __name__ == "__main__":
    main()

