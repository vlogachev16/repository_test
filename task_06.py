#  Задан целочисленный список c n случайных
#  элементов. Определить количество участков списка,
#  на котором элементы монотонно возрастают (каждое
#  следующее число больше предыдущего).

from random import randint

list = []
for i in range(10):
    list.append(randint(0, 100))
print(list)

i = 0
sum = 0
c = 1

while c < len(list):
    if list[i] < list[c]:
        sum += 1
    c += 1
    i += 1
print(sum)
