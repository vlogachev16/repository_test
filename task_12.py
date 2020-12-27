#Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
#'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого
#ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
#получить список ключей - использовать метод .keys()

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}

a = len(my_dict)

i = 0

to_list = list(my_dict.keys())

while i < a:
    c = len(to_list[i])
    d = to_list[i] + str(c)
    my_dict[d] = my_dict.pop(to_list[i])
    i += 1



print(my_dict)
