# Basic try/except
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("This always runs!")

# Custom exception handling
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Valid age:", age)

try:
    check_age(21)
    check_age(-5)
except ValueError as e:
    print("Caught an error:", e)