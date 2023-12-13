# Simple Calculator using while loop
while True:
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    valid_operaters = ('1', '2', '3', '4')
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice (1/2/3/4): ")
        if choice in valid_operaters:
            break
        print("Invalid Input")

    if choice == '1':
        print(num1, "+", num2, "=", num1+num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1-num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1*num2)
    elif choice == '4':
        print(num1, "/", num2, "=", num1/num2)
    else:
        print("Invalid Input")
    print("Do you want to continue?")
    want_to_continue = input("Press Y for yes and N for no: ")
    if want_to_continue == 'N':
        break
    print('Thank you for using Simple Calculator')
