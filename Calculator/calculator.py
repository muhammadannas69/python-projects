# Create a calculator that performs:
# Addition
# Subtraction
# Multiplication
# Division
# Requirements
# Handle invalid numeric input.
# Handle division by zero.
# Keep running until the user chooses to exit.
# Hint:
# Use try-except for user input and division.
# Use if-else to validate the selected operation.
# print(" calculator  ")
t = True
try:
    while t:
        print("for Addition press 1")
        print("for subtraction 2")
        print("for division 3")
        print("for multiplcation 4")
        print("for exit 0")
        user = int(input("what you want ="))
       
        if user == 0:
            break
        num1 = int(input("Enter a First number "))
        num2 = int(input("Enter a second number "))
        if user == 1:
            add = num1 + num2
            print(f"the sum of {num1} + {num2} = {add}")
        elif user == 2:
            sub = num1 - num2
            print(f"The subtraction of {num1} - {num2} = {sub}")
        elif user == 3:
            divid = float(num1/num2)
            print(f"the division of {num1} / {num2} = {divid}")
        elif user == 4:
            multi = num1*num2
            print(f"the product of {num1} * {num2} = {multi}")
           
except ValueError:
    print("invalid numreric please Enter a number")
except ZeroDivisionError:
    print("division by zero not allowed")
else:
    print("you close your program")
finally:
    print("program close")
