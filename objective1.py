from math import *

class polygon:
    """
    This class calculates the interior angle ,
    apothem , perimeter, area 
    """
    def __init__(self,n,r):
        self.n = n
        if n < 3:
            raise ValueError("n must be greater then 3")
        self.r = r
        self.edges = self.n
        self.vertices = self.n
        self.edge_length = self.calculate_edge_length()
        self.interior_angle = self.calculate_interior_angle()
        self.apothem = self.calculate_apothem()
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()
    def calculate_interior_angle(self):
        ia = (self.n - 2)*(180/self.n)
        return ia
    def calculate_edge_length(self):
        s = 2*self.r*sin(pi/self.n)
        return s
    def calculate_apothem(self):
        a = self.r * cos(pi/self.n)
        return a
    # @property
    def calculate_area(self):
        s = self.calculate_edge_length()
        a = self.calculate_apothem()
        ar = (self.n * s * a)/2
        return (ar)
    # @property
    def calculate_perimeter(self):
        s = self.calculate_edge_length()
        per = self.n * s
        return (per)
    def __repr__(self):
        return f'No of sides :{self.n} , Radius : {self.r}'
    def __eq__(self,other):
        return (self.n == other.n) and (self.r == other.r)
    def __gt__(self,other):
        return (self.n > other.n)
    