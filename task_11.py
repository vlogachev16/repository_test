# Дан список целых чисел. Подсчитать сколько четных
# чисел в списке

my_list = [2, 4, 6, 7, 8, 9, 100]

a = len(my_list)

i = 0

count_num = 0

while i < a:
    if my_list[i] % 2 == 0:
        count_num = count_num + 1
    i += 1
print (count_num)
