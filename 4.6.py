# 1) итератор, генерирующий целые числа, начиная с указанного,
# 2) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle

def my_count_func(start_number):
    for el in count(start_number +1):
        if el > 10:
            break
        else:
            print(el)

def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1

my_count_func(start_number = int(input("Введите начальное значение: ")))
my_cycle_func(my_list = [1, 2, 3, 4, 5], iteration = int(input("Введите значение: ")))