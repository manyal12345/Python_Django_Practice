# Simple Calculater
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operater = input("Enter operater: '+' '-' '*' '/' ")

def simple_calculater(num1, num2, operater):
    if operater == "+":
        return int(num1) + int(num2)
    elif operater == "-":
        return int(num1) - int(num2)
    elif operater == "*":
        return int(num1) * int(num2)
    elif operater == "/":
        return int(num1) / int(num2)
    else:
        print("Invalid Input")

simple_calculater(num1, num2, operater)