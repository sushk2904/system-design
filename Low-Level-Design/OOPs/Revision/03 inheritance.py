class Animal:
    def eat(self):
        print("I'm eating")
    
    def sleep(self):
        print("I'm sleeping")

class Dog(Animal):
    def bark(self):
        print("The dog is barking")

d1 = Dog()
d1.bark()
d1.eat()
d1.sleep()