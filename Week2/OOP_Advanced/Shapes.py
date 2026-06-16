class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
       print("0") 

    def __str__(self):
        return f"{self.name}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")  
        self.width = width
        self.height = height

    def area(self):                     
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):                    
        return 3.14159 * (self.radius ** 2)
    
rect = Rectangle(6, 4)
circ = Circle(5)
print(rect)   
print(circ)    
shapes = [rect, circ]

for shape in shapes:
    print(f"{shape.name} area: {shape.area():}")