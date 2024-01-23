class Animal:
    def walk(self):
        print("The animal is walking.")

class Dog(Animal):
    def bark(self):
        print("The dog barks.")

class Cat(Animal):
    pass #nothing and dont worry about it

meow = Cat()
meow.walk()
bhow = Dog()
bhow.walk()
bhow.bark()