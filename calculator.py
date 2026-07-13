print("=========================================")
print("        PYTHON CALCULATOR")
print("=========================================")

num1 = float(input("Enter first number:  "))
operator = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2  !=  0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
print("\nDo you want to perform another calculation?")
answer = input("Enter Y for Yes or N for No: ")

if answer == "Y" or answer == "y":
    print("Restart the program to calculate again.")
elif answer == "N" or answer == "n":
    print("Thank you for using the Python Calculator!")
else:
    print("Invalid selection.")
