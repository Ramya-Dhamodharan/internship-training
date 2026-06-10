print("=== Multiplication Table ===")
number = int(input("Which times table? "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("===Sum 1 to 100===")
total=0
for i in range (1,101):
    total+=i
print("The sum of numbers from 1 to 100 is:", total)

print("======FizzBuzz from 1 to 50======")
for i in range (1,51):
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:       
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)


print("======GuessingGame======")
target=13
attempts=0
print ("I'm thinking of a number between 1 and 20. Can you guess it?")
while True:
    guess = int(input("Enter your guess:"))
    attempts+=1
    if (guess==target):
        print("Congratulations! You guessed the number in ",attempts," attempts.")
    elif (guess<target):
        print("Higher")
    elif (guess>target):
        print("Lower")
    