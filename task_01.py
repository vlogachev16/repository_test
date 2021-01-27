# Создать три класса, описывающие реальные объекты. Каждый класс должен содержать
# минимум три приватных атрибута, конструктор, геттеры и сеттеры для каждого
# атрибута, два метода.

class Laptop():
    """

    A Class used to represent laptops of different brands

    """

    def __init__(self, brand, RAM, ssd):
        self.__brand = brand
        self.__RAM = RAM
        self.__ssd = ssd


    def get_brand(self)->str:
        """

        function returns the current value of the variable 'brand'

        Parameters

        ----------

        no parameters

        Return
        ------

        value of the variable 'brand' - > str

        """
        return self.__brand


    def set_brand(self, brand) -> None:
        """

        Use the function if it's necessary to change a value of the
        variable 'brand'

        Parameters

        ----------

        Enter a new 'brand' -> str

        Return
        ------

        the function changes value of the 'brand' variable

        the function returns None

        """
        self.__brand = brand


    def get_RAM(self) -> int:
        """

        function returns value of the variable 'RAM'

        Parameters

        ----------

        no parameters

        Return
        ------

        value of the variable 'brand' ->

        """
        return self.__RAM


    def set_RAM(self, RAM):
        self.__RAM = RAM

    def get_disk(self):
        return self.__ssd


    def set_disk(self, ssd):
        self.__ssd = ssd


    def change_ram(self):
        self.__RAM *= 2
        return self.__RAM


    def change_ssd(self):
        self.__ssd *= 2
        return self.__ssd

class Cars():
    def __init__(self, brand, model, year_issue):
        self.__brand = brand
        self.__model = model
        self.__year_issue = year_issue

    @property
    def get_brand(self):
        return self.__brand


    def set_brand(self, brand):
        self.__brand = brand


    def get_model(self):
        return self.__model


    def set_model(self, model):
        self.__model = model

    def get_year_issue(self):
        return self.__year_issue


    def set_year_issue(self, year_issue):
        self.__year_issue = year_issue


    def start_car(self):
        print('VVVRUUUM!!!')
    @property
    def shut_down_car(self):
        print('vshushush')

class Games():
    def __init__(self, name, game_genre, year_release):
        self.__name = name
        self.__game_genre = game_genre
        self.__year_release = year_release

    def get_name(self):
        return self.__name


    def set_name(self, name):
        self.__name = name


    def get_game_genre(self):
        return self.__game_genre


    def set_game_genre(self, game_genre):
        self.__game_genre = game_genre

    def get_year_release(self):
        return self.__year_release


    def set_year_release(self, year_release):
        self.__year_release = year_release


    def start_shooting(self):
        print('peowpeowpeow!!!')
    @property
    def start_game(self):
        print('welcome to csgo')



def main():
    laptop_1 = Laptop('macbook', 16, 256)
    print(laptop_1.get_brand(), laptop_1.get_RAM(), laptop_1.get_disk())
    car_1 = Cars('Mercedes', 'S-class', 2020)
    print(car_1.get_brand, car_1.get_model())
    car_1.start_car()
    car_1.shut_down_car
    game_1 = Games('CSGO', 'Shooter', 2012 )
    print(game_1.get_name(), game_1.get_game_genre(), game_1.get_year_release())
    game_1.start_game


if __name__ == '__main__':
    main()
