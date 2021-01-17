# Написать модуль, содержащий 12 функций по переводу:
# Примечание: функция принимает на вход число и возвращает конвертированное
# число

# Дюймы в сантиметры

def inchCm(number: int) -> int:
    """Функция конвертирующая дюймы в сантиметры.

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 2.54
    return result

# print(inchCm(float(input())))

# Сантиметры в дюймы

def cmInch(number: int) -> int:
    """Функция конвертирующая сантиметры в дюймы

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 0.39
    return result

# print(cmInch(float(input())))

# Мили в километры

def milesKm(number: int) -> int:
    """Функция конвертирующая мили в километры

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 1.60
    return result

# print(milesKm(float(input())))

# Километры в мили

def kmMiles(number: int) -> int:
    """Функция конвертирующая километры в мили

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 0.62
    return result

# print(kmMiles(float(input())))


# Фунты в килограммы

def poundKg(number: int) -> int:
    """Функция конвертирующая фунты в килограммы

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 0.45
    return result

# print(poundKg(float(input())))

# Килограммы в фунты

def kgPound(number: int) -> int:
    """Функция конвертирующая килограммы в фунты

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 2.20
    return result

# Унции в граммы

def ounceGr(number: int) -> int:
    """Функция конвертирующая унции в граммы

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 28
    return result

# Граммы в Унции

def grOunce(number: int) -> int:
    """Функция конвертирующая граммы в унции
    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 0.03
    return result

# Галлон в литры

def gallonL(number: int) -> int:
    """Функция конвертирующая галлоны в литры

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 3.78
    return result

# Литр в галлоны

def lGallon(number: int) -> int:
    """Функция конвертирующая литры в галлоны

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 0.26
    return result

# Пинты в литры

def pintL(number: int) -> int:
    """Функция конвертирующая пинты в литры

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 0.47
    return result

# Литры в Пинты

def lPint(number: int) -> int:
    """Функция конвертирующая литры в пинты

    Parameters
    ----------

    number: int

    Returns
    -------

    Возвращает результат вычесления (float)"""

    result = number * 2.11
    return result



print('Ноль в качестве варианта перевода'
      '\nзавершит работу программы!!!')
while True:
    a = input('Варианты перевода:' '\n1) Дюймы в сантиметры'
    '\n2) Сантиметры в дюймы''\n3) Мили в километры'
    '\n4) Километры в мили' '\n5) Фунты в килограммы'
    '\n6) Килограммы в фунты' '\n7) Унции в граммы' '\n8) Граммы в унции'
    '\n9) Галлон в литры''\n10) Литры в галлоны' '\n11) Пинты в литры'
    '\n12) Литры в пинты'
    '\nВведите вариант перевода:')
    if a == '0':
        break
    if a in '1':
        print(inchCm(float(input())))
    elif a in '2':
        print(cmInch(float(input())))
    elif a in '3':
         print(milesKm(float(input())))
    elif a in '4':
        print(kmMiles(float(input())))
    elif a in '5':
        print(poundKg(float(input())))
    elif a in '6':
        print(kgPound(float(input())))
    elif a in '7':
        print(ounceGr(float(input())))
    elif a in '8':
        print(grOunce(float(input())))
    elif a in '9':
        print(gallonL(float(input())))
    elif a in '10':
        print(lGallon(float(input())))
    elif a in '11':
        print(pintL(float(input())))
    elif a in '12':
        print(lPint(float(input())))

def main():
    if __name__ == '__main__':
        inchCm()

def main():
    if __name__ == '__main__':
        cmInch()

def main():
    if __name__ == '__main__':
        milesKm()

def main():
    if __name__ == '__main__':
        kmMiles()
def main():
    if __name__ == '__main__':
        poundKg()

def main():
    if __name__ == '__main__':
        kgPound()

def main():
    if __name__ == '__main__':
        ounceGr()

def main():
    if __name__ == '__main__':
        grOunce()

def main():
    if __name__ == '__main__':
        gallonL()

def main():
    if __name__ == '__main__':
        lGallon()

def main():
    if __name__ == '__main__':
        pintL()
def main():
    if __name__ == '__main__':
        lPint()
