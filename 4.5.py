# Вывести список всех чётных чисел от 100 до 1000 и их произведение

from functools import reduce

def my_func(el_p, el):
    return el_p * el

print(f'Список четных чисел: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')