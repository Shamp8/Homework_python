# Сумма двух наибольших аргументов

def sum_arg(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат - {sum_arg(int(input("Введите первое значение: ")), int(input("Введите следующее значение: ")), int(input("Введите следующее значение: ")))}')