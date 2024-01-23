class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("Move")
    
    def draw(self):
        print("Draw")
        
    def corrdinates(self):
        print(self.x)
        print(self.y)

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"{self.name} is talking")


# p1 = Point(10,20)
# p1.draw()
# p1.move()
# p1.corrdinates()

annu = Person("Ananya")
annu.talk()
    