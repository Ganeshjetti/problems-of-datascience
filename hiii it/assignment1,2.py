class Polygon:
    def area(self):
        NotImplemented  
    def perimeter(self):
        NotImplemented  
    def __str__(self):
        return ("Polygon")
class Triangle(Polygon):
    def __init__(self,height,base,side1,side2,side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3   
    def area(self):
        return (0.5 * self.base * self.height)
    def perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    def __str__(self):
        return ("Triangle")
class Rectangle(Triangle):
    def __init__(self, length, width):
        super().__init__(length, width, length, width, length+width)
        self.length = length
        self.width = width  
    def area(self):
        return (self.length * self.width )
    def perimeter(self):
        return (2 * (self.length + self.width))
    def __str__(self):
        return ("Rectangle")
traingle = Triangle(5,6,5,6,8)
rectangle = Rectangle(5,6)
#polygon = Polygon()
#print (f"Type : {traingle}, Area : {traingle.area()}, Perimeter : {traingle.perimeter()}")
#print (f"Type : {rectangle}, Area : {rectangle.area()}, Perimeter : {rectangle.perimeter()}")
#print(f"Type : {polygon}, Area : {polygon.area()}, Perimeter : {polygon.perimeter()}")

def print_polygon_info(polygon):
    print(f"Type: {polygon}, Area: {polygon.area()}, Perimeter: {polygon.perimeter()}")
print_polygon_info(traingle)
print_polygon_info(rectangle)