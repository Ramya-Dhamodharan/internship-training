# Basic function
def greet(name):
    print("Hello,", name)

greet("Ramya")
greet("Intern")

# Function with return value
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# Function with default argument
def greet_intern(name, role="Intern"):
    print(f"Welcome {name}, you are a {role}")

greet_intern("Ramya")
greet_intern("Ramya", "Developer")