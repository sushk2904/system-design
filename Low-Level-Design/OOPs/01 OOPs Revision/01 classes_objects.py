class Student:
    #Variable under class are called atrributes
    name = ""
    age = 0
    gender = ""

    #Methods
    def display(self):
        print("This is a display function")
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

s1 = Student()
print(s1)
print(s1.name)
print(s1.age)
print(s1.gender)





#More optimized way of writing classes and objects
class Studentt:
    #defining attributes
    name = ""
    age =  0
    gender = ""

    def set_info(self):
        self.name = input("Enter the name:")
        self.age = int(input("Enter your age:"))
        self.gender = input("Enter your gender:")

    def displayy(self):
        print(f"self = {self}")
        print(f"The name of student is {self.name}, the age is {self.age} and the gender is {self.gender} ")
    
    def set_info_with_parameters(self, naam, age, gender):
        self.name = naam
        self.age = age
        self.gender =  gender
    
    def set_info_with_parameters_and_annotations(self, naam: str, age: int, gender: str):
        self.name = naam
        self.age = age
        self.gender =  gender
    
s1 = Studentt()
s1.name =  "bodmosh"
s1.age =  18
s1.gender = "male"

print(s1)
s1.displayy()


s2 = Studentt()
s2.set_info()
s2.displayy()

s3 = Studentt()
s3.set_info_with_parameters("Bodmosh2", 19, "mard")
s3.displayy()


#Best way to define a method
class Car:
    
    #Method/Initializer 
    def __init__(self, name: str, year: str, oil: str) -> None:
        self.model = name
        self.manufactured = year
        self.oil = oil
    
    def display(self) -> None:
        print(f"The name of the vehicle is {self.model}, the year it is manufactured is {self.manufactured} and its running oil type is {self.oil}")
    
c1 = Car("Maybach", 2026, "Petrol")
c1.display()