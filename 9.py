import random

a = list(range(0, 100))
random.shuffle(a)

print(a[:10])
b = int(input('Введите порядковый номер любого числа из списка '))

a[int(b)] = int(b)
print(a[:10])
