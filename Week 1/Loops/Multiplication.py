print("=== Multiplication Table ===")
number = int(input("Which times table? "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("===Sum 1 to 100===")
total=0
for i in range (1,101):
    total+=i
print("The sum of numbers from 1 to 100 is:", total)  