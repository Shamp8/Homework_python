# Сумма чисел введённых в строку
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите значение или q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
    print('Сумма = ', sum_res)
my_sum()