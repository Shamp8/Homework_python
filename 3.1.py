# Деление двух чисел
def div(x, y):
    try:
        z = round (x / y, 3)
        return z
    except ZeroDivisionError:
        return "Деление на ноль"
print(div(int(input("Введите делимое: ")), (int(input("Введите делитель: ")))))




