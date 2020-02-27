class Circle():
    def __init__(self, radius, pi=3.14):
        self.r = radius
        self.pi = pi
 
    def area(self):
        return self.pi * self.r**2
        
    def perimeter(self):
        return 2 * self.pi * self.r
        
Circle1 = Circle(5)
print(Circle1.area())
print(round(Circle1.perimeter(),2))
