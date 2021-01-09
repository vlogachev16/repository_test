from random import randint

matrix = []

n = int(input())

for i in range(n):
    line = []
    for j in range(n):
        line.append(randint(0, 20))
    matrix.append(line)

print(matrix)

r = 0

for d in matrix:
    matrix[r][r] = max(matrix[r])
    r += 1
print(matrix)
