# Создать класс Car. Атрибуты: марка, модель, год выпуска,
# скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5),
# уменьшение скорости(скорость - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.

class Car():
    default_speed = 0
    def __init__(self, brand, model, year_issue, speed):
        self.__brand = brand
        self.__model = model
        self.__year_issue = year_issue
        self.__speed = speed

    @property
    def speed_increase(self):
        self.__speed += 5
        return self.__speed

    @property
    def speed_decrease(self):
        self.__speed -= 5
        return self.__speed

    @property
    def speed_reset(self):
        self.__speed = 0
        return self.__speed
    @property
    def get_speed(self):
        return self.__speed
    @property
    def opposite_speed(self):
        opposite_speed = self.__speed - self.__speed * 2
        return opposite_speed

def main():
    car_1 = Car('mazda', 6, 1999, 10)
    print(car_1.opposite_speed)

if __name__ == '__main__':
    main()
