#  Для каждого натурального числа в промежутке от m до
#  n вывести все делители, кроме единицы и самого
#  числа. m и n вводятся с клавиатуры.
#  Пример:m =100, n = 105

m = int(input())
n = int(input())
list = []
for i in range(m,n + 1):
    list.append(i)
print(list)


for i in list:
    a = []
    d = 2
    while d < n and i != d:

        if i % d == 0:
            a.append(d)
        d += 1

    print(a)
