# Дан список. Создать новый список, сдвинутый на 1 элемент влево.
# Пример 1 2 3 4 5 -> 2 3 4 5 1

my_list = [1,2,3,4,5]

my_list_len = len(my_list)

new_list = []

i = 0

while i <  my_list_len:
    if i + 1 == my_list_len:
        new_list.append(my_list[0])
    else:
        new_list.append(my_list[i + 1])
    i += 1

print(new_list)
