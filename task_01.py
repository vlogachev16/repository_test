# Описать функцию fact2(n), вычисляющую двойной
# факториал: n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 — параметр целого типа).
# С помощью этой функции найти двойные факториалы пяти случайных целых чисел.

def fact2(n: int) -> int:
    """функция для вычсиления двойного факторила

    Parameters
    ----------

    n: int

    Return
    ------

    возвращает итоговый результат (int)"""
    counter = 1
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                counter *= i
    else:
        if n % 2 != 0:
            for i in range (1, n+1):
                if i % 2 != 0:
                    counter *= i
    return counter

print(fact2(int(input())))

def main():
    if __name__ == '__main__':
        fact2()
