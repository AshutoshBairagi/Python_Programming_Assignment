'''
Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print the area
of the shape where Shape&#39;s area is 0 by default.
'''

class Shape():
    def default_area(self):
        return "Default area of shape is "+str(0)
class Square(Shape):
    def __init__(self,length):
        self.length = length

    def default_area(self):
        return "Default area of square is "+str(0)
    def area_by_length(self):
        return "Area of square is "+str((self.length**2))

shape_obj = Shape()
square_obj = Square(10)
print(shape_obj.default_area())
print(square_obj.default_area())
print(square_obj.area_by_length())

