class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name," makes a sound.")

    def __str__(self):
        return "Animal named", self.name


class Dog(Animal):
  
    def __init__(self, name, breed):
        super().__init__(name)    
        self.breed = breed        

    def speak(self):            
        print(self.name," says Woof!")

    def __str__(self):            
        return  f"Dog named {self.name} {self.breed}"

class Cat(Animal):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):              
        print(self.name," says Meow!")
    
    def __str__(self):            
        return  f"Cat named {self.name} {self.color}"

dog1 = Dog("Rex", "Labrador")
cat1 = Cat("Whiskers", "Black")
dog2 = Dog("Buddy", "Beagle")

print(dog1)       
print(cat1) 
dog1.speak()       
cat1.speak()       

animals = [dog1, cat1, dog2]   
for animal in animals:
    animal.speak()            
