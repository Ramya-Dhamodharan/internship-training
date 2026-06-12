print("======Login System======")
user = "admin"
passcode = "password123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == user and password == passcode:
    print("Login successful!")
else:
    print("Invalid username or password.")