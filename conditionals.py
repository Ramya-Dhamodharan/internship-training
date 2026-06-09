print("======Number Classifier======")
number= int(input("Enter a number:"))
if(number<0):
    print("The given number is Negative")
elif(number==0):
    print("The given number is Zero")
elif(number>0):
    print("The given number is positive")

print ("======Even or Odd Classifier======")
number= int(input("Enter a number:"))
if(number%2==0):
    print("The given number is Even")
else:
    print("The given number is Odd")

print("======Grade Classifier======")
score= int(input("Enter your score:"))
if(score>=90):
    print("Your grade is A")
elif(score>=80):
    print("Your grade is B")
else:
    print("Your grade is C")




print("======Login System======")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password.")


print("======Largest Number Classifier======")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:  
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)