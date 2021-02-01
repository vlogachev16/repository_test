from classes import *

cir_1 = Circle(2, 3, 5, 3, 4, 6)
# print('периметр круга:',cir_1.perimeter())
# print('площадь круга:',cir_1.area())
triangle_1 = Triangle(2,3,5,3,4,6)
# print('периметр треугольника:',triangle_1.perimeter())
# print('площадь треугольника:',triangle_1.area())
square_1 = Square(2, 3, 5, 3, 4, 6)
# print('периметр квадрата:',square_1.perimeter())
# print('площадь квадрата:',square_1.area())

area_cir = cir_1.area()
area_triangle = triangle_1.area()
area_square = square_1.area()

list = ['Circle', 'Triangle', 'Square']


def main():
    for i in list:
        if  i == 'Circle':
            print(f'circle -> {cir_1.area()}')
        elif i == 'Triangle':
            print(f'triangle -> {triangle_1.area()}')
        elif i == 'Square':
            print(f'square -> {square_1.area()}')

if __name__ == '__main__':
    main()
