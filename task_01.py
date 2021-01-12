# Написать модуль, содержащий 12 функций по переводу:
# Примечание: функция принимает на вход число и возвращает конвертированное
# число

# Дюймы в сантиметры

def inchCm(number):
    result = number * 2.54
    return result

# print(inchCm(float(input())))

# Сантиметры в дюймы

def cmInch(number):
    result = number * 0.39
    return result

# print(cmInch(float(input())))

# Мили в километры

def milesKm(number):
    result = number * 1.60
    return result

# print(milesKm(float(input())))

# Километры в мили

def kmMiles(number):
    result = number * 0.62
    return result

# print(kmMiles(float(input())))


# Фунты в килограммы

def poundKg(number):
    result = number * 0.45
    return result

# print(poundKg(float(input())))

# Килограммы в фунты

def kgPound(number):
    result = number * 2.20
    return result

# Унции в граммы

def ounceGr(number):
    result = number * 28
    return result

# Граммы в Унции

def grOunce(number):
    result = number * 0.03
    return result

# Галлон в литры

def gallonL(number):
    result = number * 3.78
    return result

# Литр в галлоны

def lGallon(number):
    result = number * 0.26
    return result

# Пинты в литры

def pintL(number):
    result = number * 0.47
    return result

# Литры в Пинты

def lPint(number):
    result = number * 2.11
    return result
