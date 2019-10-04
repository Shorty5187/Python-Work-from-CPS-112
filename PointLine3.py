import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x,self.y)

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def distance(self, other_point):
        delta_x = self.x - other_point.x
        delta_y = self.y - other_point.y

        return math.sqrt(delta_x**2 + delta_y**2)

    @classmethod
    def distance2(cls, pt1, pt2):
        delta_x = pt1.x - pt2.x
        delta_y = pt1.y - pt2.y

        return math.sqrt(delta_x **2 + delta_y**2)

class Line: #y = mx + b

    def __init__(self, slope, yint):
        self.slope = slope
        self.yint = yint

    def pointfunction(self, pt1, pt2):
        self.y()
        self.x()
        pt1 = line1
        pt2= line2

        return (pt1, pt2)

    def __str__(self):
        return '(y = {}x + {})'.format(self.slope, self.yint)

    def xint(self): #give the x-intercept of this line
        # x_axis is a Line object
        x_axis = Line(slope = 0, yint = 0)
        # intercept is a Point object
        intercept = self.intersection(x_axis)
        # x_val is a float
        x_val = intercept.x
        return x_val

    def y(self, x):#gives you y for an input of x
        return self.slope * x + self.yint

    def x(self, y):
        return (y - self.yint) / self.slope

    def intersection(self, other_line):
        if self.slope == other_line.slope:
            if self.yint == other_line.yint:
                raise Exception("Same Line")
            else:
                raise Exception("Parallel Lines")
        else:
            x = (self.yint - other_line.yint) / (other_line.slope - self.slope)
            y = self.y(x)
            return Point(x,y)

#code to print a point
#pt = Line(line1, line2)
#a = 10
#b = 0
#if b == 0:
#    raise Exception("Horizontal Line")
#else:
#    c = a/b
# try:
#     c = a/b
#     print(c)
# except:
#     print('problem...')
# pt1 = Point(2,3)
# pt2 = Point(5,7)
#
# line4 = Line(pt1, pt2)
#
# print(pt1)
# print('x =', pt1.x)
# print('y =', pt1.y)
#
# pt1.move(4,-2)
# print(pt1)
#
# dist = pt1.distance(pt2)
# print('distance is', dist)
#
# dist = Point.distance2(pt1, pt2)
# print('distance is', dist)
#Test code for line class program
line1 = Line(2, 3)
print(line1)
print(line1.xint())
# line2 = Line(5, 8)
# print(line2.intersection(line1))
# print(line1.y(6))
# print(line1.x(15))
# #line3 = Line(2, 6)
# #line1.intersection(line3)
# line1.intersection(Line(2, 6))
