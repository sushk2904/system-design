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

    def displayy(self):
        print(f"self = {self}")
        print(f"The name of student is{self.name}, the age is {self.age} and the gender is {self.gender} ")
    
s1 = Studentt()
s1.name =  "bodmosh"
s1.age =  18
s1.gender = "male"

print(s1)
s1.displayy()