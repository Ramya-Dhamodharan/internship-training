

class Student:
   

    def __init__(self, name, grade):
        
        self.name = name
        self.grade = grade

    def study(self):
       
        print(f"{self.name} is studying hard to maintain {self.grade} grade!")

    def display_info(self):
        print(f"Student: {self.name} | Grade: {self.grade}")









