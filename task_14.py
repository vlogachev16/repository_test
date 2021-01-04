# Составить список чисел Фибоначчи содержащий 15 элементов.

fib_list = [1,1]

i = 0

while len(fib_list) < 15:
    fib_list.append(fib_list[-1] + fib_list[-2])

print(fib_list)

#

fib_list_for = [1,1]  #[1,1,2,3,5,8,13,21,34]

i = 0

for num in range(15 - len(fib_list_for)):
    fib_list_for.append(fib_list_for[i] + fib_list_for[-1])
    i += 1
print(fib_list_for)
