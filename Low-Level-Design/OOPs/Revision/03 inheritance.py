class Animal:

    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print("I'm eating")
    
    def sleep(self):
        print("I'm sleeping")
    
    def display(self):
        print(f"The name of the animal is {self.name} and the age of the animal is {self.age}")

class Dog(Animal):
    def bark(self):
        print("The dog is barking")


d1 = Dog("Tyson", 8)
d1.bark()
d1.eat()
d1.sleep()

