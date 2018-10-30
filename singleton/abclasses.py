from abc import ABCMeta, abstractmethod

class Shape(object):
    """
    This practice work was created to show how to realize abstract classes.
    It is realized by principle of inheritance chain.
    Shape --↓
             Rectangle --↓
                          Square

    Class Shape is aimed mainly for parent class and consisits of abstract methods for using inherited classes.
    
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod  
    def perimeter(self): pass

class Rectangle(Shape):
    """
    Class Rectangle is an inherited class, which initializes the width and height.
    It inherits the abstract methods from parent classes.
    Also, returns the actual area and perimeter of the rectangle by the help of formula. 
    """
    def __init__(self, width, height):
        self.width=width
        self.height=height

        super(Rectangle, self).__init__()
    def area(self):
        print("Using Rectangle area method:")
        return self.width * self.height
    
    def perimeter(self):
        print("Using Rectangle perimeter method")
        return self.width*2+self.height*2
    
class Square(Rectangle):
    """
    Class Square is an inherited class, which initializes the width and height.
    It inherites the abstract methods from the Rectangle class, because their shape is similiar. 
    Also, returns the actual area and perimeter of the square. 
    """
    def __init__(self, side_length):
        self.side_length=side_length
        super(Square, self).__init__(side_length, side_length)
        
    def area(self):
        print("Using Square area method:")
        return self.width*self.height
    
    def perimeter(self):
        print("Using Square perimeter method:")
        return self.width*2+self.height*2
        
        
def main():
    rect=Rectangle(5,6)
    print(rect.area())
    s=Square(4)
    print(s.area())
if __name__=="__main__":
    main()

