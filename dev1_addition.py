# dev1_addition.py

def add(a, b):
    return a + b

try:
    # Taking input from user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Calling the function and displaying result
    print("The sum is:", add(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")
