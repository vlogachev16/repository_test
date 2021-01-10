#  В заданной строке расположить в обратном порядке
#  все слова. Разделителями слов считаются пробелы.



some_str = str(input())
b = list(some_str.split())
i = len(b) - 1
c = []
while i >= 0:
    c.append(b[i])
    i -= 1
#print(c)
str = ''
for h in c:
    str += f'{h} '
print(str)



# print(*reversed(a.split()))
