# Class definition
class Intern:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill

    def introduce(self):
        print(f"Hi, I am {self.name}, age {self.age}, learning {self.skill}")

    def add_skill(self, new_skill):
        self.skill = new_skill
        print(f"{self.name} is now learning {self.skill}")

# Creating objects
intern1 = Intern("Ramya", 21, "Python")
intern2 = Intern("John", 22, "React")

intern1.introduce()
intern2.introduce()

intern1.add_skill("FastAPI")
intern1.introduce()