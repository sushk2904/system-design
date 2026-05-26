class Animal:

    
    def __init__(self, name:str, age:int) -> None:
        print(f"Animal INIT")
        self.name = name
        self.age = age

    def eat(self):
        print("I'm eating")
    
    def sleep(self):
        print("I'm sleeping")
    
    def display(self):
        print(f"The name of the animal is {self.name} and the age of the animal is {self.age}")

class Dog(Animal):

    def __init__(self, name:str, age:int, breed:str) -> None:
        print(f"this is dog init")
        super().__init__(name, age) 
        """only use this when you have to set something different from the class but also want to include
        some features from the class since this def __init__ cancel outs the initial def __init for this class
        that's why we have to say super().__init__(parameter1, parameter2, .... parameter_x) to inherit the 
        initial class parameters"""
        self.breed = breed


    
    def bark(self):
        print("The dog is barking")

#From here we can conclude that we can inherit both methods and attributes

d1 = Dog("cherry",8, "Husky" )
d1.display()

