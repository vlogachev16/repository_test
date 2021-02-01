from math import sqrt
from typing import Union

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    def __init__(self, x1: Union[int,float], y1: Union[int,float],
    x2: Union[int,float], y2: Union[int,float], x3: Union[int,float],
    y3: Union[int,float]) -> Union[int,float]:

        """ looks for distance between points.

        Parameters
        ----------

        x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6: int, float

        Return
        ------
        distance between points

        type: int, float

        """
        self.a = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.b = sqrt((x2 - x3)**2 + (y2 - y3)**2)
        self.c = sqrt((x1 - x3)**2 + (y1 - y3)**2)
        self.h = y3 - y1


class Circle(Figure):
    def perimeter(self)-> Union[int, float]:
        return self.a * 3.14 * 2
    def area(self)-> Union[int, float]:
        return 3.14 * self.a**2



class Triangle(Figure):
    def perimeter(self) -> Union[int, float]:
        return self.a + self.b + self.c
    def area(self) -> Union[int, float]:
        return self.a * 0.5 * self.h

class Square(Figure):
    def perimeter(self) -> Union[int, float]:
        return self.a * 4
    def area(self) -> Union[int, float]:
        return self.a**2
