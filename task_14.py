# Составить список чисел Фибоначчи содержащий 15 элементов.

fib_list = [1,1]

i = 0

while len(fib_list) < 15:
    fib_list.append(fib_list[-1] + fib_list[-2])

print(fib_list)
