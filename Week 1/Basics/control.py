  # if/elif/else
age = 21

if age < 18:
    print("You are a minor")
elif age == 21:
    print("You are exactly 21!")
else:
    print("You are an adult")

# for loop
skills = ["Python", "Git", "FastAPI", "React"]

for skill in skills:
    print("Learning:", skill)

# while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1