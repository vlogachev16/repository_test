# Дано число. Найти сумму и произведение его цифр

num = int(input())

b = 0
c = 1

while num > 0:
    d = num % 10
    b = b + d
    c = c * d
    num = num // 10

print("Сумма:", b)
print("Произведение:", c)
