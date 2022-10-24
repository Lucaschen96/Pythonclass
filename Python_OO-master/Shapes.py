class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def calc_perimeter(self):
        return 2 * (self._a + self.b)

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def calc_perimeter(self):
        return math.pi * self._a *2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) +"]" + str(hex(id(self)))


class Sphere(Circle):
    def calc_volume(self):
        return 4/3*math.pi*self._a**3

    def calc_surface(self):
        return 4*super().calc_surface()

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def calc_perimeter(self):
        return self._a+self.b+self.c

    def calc_surface(self):
        s = (self._a+self.b+self.c)/2
        return (s*(s-self._a)*(s-self.b)*(s-self.c))**0.5

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + "," + str(self.b) + "," + str(self.c) +"] at " + str(hex(id(self)))

class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super(EquilateralTriangle, self).__init__(a, 0, 0)
        self.b = self._a
        self.c = self._a

    def __repr__(self):
        return self.__class__.__name__ + "[a=" + str(self._a) + "] at " + str(hex(id(self)))

class Square(Rectangle):
    def __init__(self, a):
        super(Square, self).__init__(a, 0)
        self.b = self._a

    def __repr__(self):
        return self.__class__.__name__ + "[a=" + str(self._a) + "] at " + str(hex(id(self)))



t = Triangle(3, 4, 5)
print(t)
print(t.calc_surface())
print(t.calc_perimeter())
print()

et = EquilateralTriangle(6)
print(et)
print(et.calc_surface())
print(et.calc_perimeter())
print()

r = Rectangle(5, 6)
print(r)
print(r.calc_surface())
print(r.calc_perimeter())
print()
# r.swap_sides()
# r_desc = str(r)
# print(r_desc)

c = Circle(7)
# c_desc = str(c)
# print(c_desc)
print(c)
print(c.calc_surface())
print(c.calc_perimeter())
print()

s = Sphere(8)
print(s)
print('s volume: ')
print(s.calc_volume())
print('s surface:')
print(s.calc_surface())
print()

sq = Square(5)
print(sq)
print(sq.calc_perimeter())
print(sq.calc_surface())
