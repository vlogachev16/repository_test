# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен
# исходному элементу умноженному на -2

my_list = [1, 2, 4, 8, 16, 32]

a = int(len(my_list))
# print(a)

new_list = [0, 0, 0, 0, 0, 0]  # если нужно создать новый список, а не из
# менять существующий

i = 0

while i < a:
    # my_list[i] = my_list[i] * (-2)  # если хотим внести изменения в
    # существующий список
    # i += 1
     new_list[i] = my_list[i] * (-2)
     i += 1

#p rint(my_list)
print(new_list)


# Решение задачи с помощью цикла for.


list_for = []

for i in my_list:
    list_for.append(i *(-2))
print(list_for)
