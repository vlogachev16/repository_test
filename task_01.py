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
