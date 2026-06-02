import json

# Writing to a file
with open("data.txt", "w") as f:
    f.write("Hello, this is my first file!\n")
    f.write("I am learning Python!\n")

# Reading from a file
with open("data.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)

# Writing JSON
intern = {
    "name": "Ramya",
    "age": 21,
    "skills": ["Python", "Git", "FastAPI"]
}

with open("intern.json", "w") as f:
    json.dump(intern, f, indent=4)
    print("JSON file written!")

# Reading JSON
with open("intern.json", "r") as f:
    data = json.load(f)
    print("Name:", data["name"])
    print("Skills:", data["skills"])