

class Student:
   

    def __init__(self, name, grade):
        
        self.name = name
        self.grade = grade

    def study(self):
       
        print(f"{self.name} is studying hard to maintain {self.grade} grade!")

    def display_info(self):
        print(f"Student: {self.name} | Grade: {self.grade}")




student1 = Student("Ramya", "A")   
student2 = Student("Priya", "B")    

print("===== STUDENT CLASS =====")

student1.display_info()             
student2.display_info()            

student1.study()                   
student2.study()                    


print(f"{student1.name}'s grade: {student1.grade}")


student2.grade = "A"
print(f"{student2.name} improved to: {student2.grade}")




