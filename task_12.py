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

my_dict_for = {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}




for key in list(my_dict_for):
    new_key = f'{key}{len(key)}'
    my_dict_for[new_key] = my_dict_for.pop(key)

print(my_dict_for)

    #my_dict_for =  my_dict_for.pop(b)
