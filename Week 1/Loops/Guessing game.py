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
    