# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
# сложения, вычитания, умножения на число, вывод на экран.

from typing import Union

class MyTime:
    def __init__(self, hours: int, minutes: int, seconds: int) -> int:
        self.hours = hours
        self. minutes = minutes
        self.seconds = seconds

    def __eq__(self, hour_1: int) -> bool:
        return self.hours == hour_1


    def __ne__(self, minutes_1: int) -> bool:
        return self.minutes != minutes_1

    def __ge__(self, seconds_1: int) -> bool:
        return self.seconds >= seconds_1

    def __gr__(self, seconds_1: int)-> bool:
        return self.seconds > seconds_1

    def __lt__(self, seconds_1: int) -> bool:
        return self.seconds <= seconds_1

    def __le__(self, minutes_1: int) -> bool:
        return self.minutes < minutes_1

    def __add__(self, hour_1: int) -> int:
        return self.hours + hour_1

    def __sub__(self, minutes_1: int) -> int:
        return self.minutes - minutes_1

    def __mul__(self, seconds_1: int) -> int:
        return self.seconds * seconds_1


def main() -> Union[bool, int]:
    mytime_1 = MyTime(2, 11, 29)
    print(mytime_1 == 10)


if __name__ == '__main__':
    main()
