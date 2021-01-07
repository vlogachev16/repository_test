#  В списке целых случайных чисел с количеством
#  элементов n определить максимальное число и
#  заменить им все четные по значению элементы.

from random import randint

list = []
for i in range(20):
    list.append(randint(0, 20))

b = max(list)  # максимальное число в списке

print(b)

d = 0

for i in list:
    if i % 2 == 0:
        list[d] = b
    d += 1
print(list)
