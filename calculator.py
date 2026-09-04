print("=========================================")
print("        PYTHON CALCULATOR")
print("=========================================")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ").strip()
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    raise SystemExit

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")

print("\nDo you want to perform another calculation?")
answer = input("Enter Y for Yes or N for No: ").strip().lower()

if answer == "y":
    print("Restart the program to calculate again.")
elif answer == "n":
    print("Thank you for using the Python Calculator!")
else:
    print("Invalid selection.")
