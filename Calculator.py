"""
This is a calculator program that performs basic arithmetic operations.
"""

def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b 

def division(a, b):
    return a/b

def calculator():
    numberA = int(input("Choose the first number: "))
    numberB = int(input("Choose the second number: "))
    choice = int(input("What would you like to do? \n1) for addition\n2) for subtraction\n3) for multiplication\n4) for division: "))
    if choice == 1:
        print(addition(numberA, numberB))
    elif choice == 2:
        print(subtraction(numberA, numberB))
    elif choice == 3:
        print(multiplication(numberA, numberB))
    elif choice == 4:
        print(division(numberA, numberB))


calculator()
