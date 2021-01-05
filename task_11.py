# Дан список целых чисел. Подсчитать сколько четных чисел в списке


my_list = [2, 4, 6, 7, 8, 9, 100]

a = len(my_list)

i = 0

count_num = 0

while i < a:
    if my_list[i] % 2 == 0:
        count_num = count_num +1
    i += 1

print(count_num)

# Решение с помощью цикла for


sum = 0

for item in my_list:
    if item % 2 == 0:
        sum += 1
print(sum)
