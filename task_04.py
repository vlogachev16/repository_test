# Вычислить значения нижеприведенной функции в диапазоне значений
# x от -10 до 10 включительно с шагом, равным 1.
# y = x2 при -5 <= x <= 5; y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# В качестве результат вывести на экран значение функции y
# при каждом x из указанного диапазона.

import math

def calculations():
    """Функция вычисляет переменную y и выводит значение переменной на
    каждой итерации в диапазоне от -10 до 10 включительно.

    Parameters

    ----------

    Функция не принимает входных параметров.

    Return
    ------

    Функция возвращает последнее значение переменной y (int)"""

    for x in range(-10, 11):
        if x >= -5 and x <= 5:
            y = x**2
            print (y)
        elif x < -5:
            y = 2 * math.fabs(x) - 1
            print(y)
        elif x > 5:
            y = 2*x
            print(y)

    return y
print(calculations())

def main():
    if __name__ == '__main__':
        calculations()
