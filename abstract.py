from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class Square(shape):
    def __init__(self,side):
        self.__side=side
    def area(self):
        return self.__side *self.__side
    def perimeter(self): 
        return self.__side*3    

sq=Square(5)
print(sq.area())
print(sq.perimeter())

