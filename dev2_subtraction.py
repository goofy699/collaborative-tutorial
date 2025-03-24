# dev2_subtraction.py

def subtract(a, b):
    return a - b

# Input and subtraction with error handling
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"Result: {a} - {b} = {subtract(a, b)}")
except ValueError:
    print("Invalid input! Please enter numerical values.")
