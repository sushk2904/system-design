from abc import *
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass    

#Concrete classes
class Rectangle(Shape):
    def __init__(self, length:int, breadth:int) -> None:
        self.length : int = length
        self.breadth :int = breadth
    
    def area(self):
        print(self.length*self.breadth)
    
    #Try commenting the whole def perimeter function and then try running
    def perimeter(self):
        print(2*(self.length + self.breadth))

r1 = Rectangle(5,2)
r1.area()

