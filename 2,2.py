number = int(input("Введите количество значений в списке: "))
example = []
i = 0
n = 0
while i < number:
    example.append(input("Введите значение для списка "))
    i += 1

for elem in range(int(len(example)/2)):
        example[n], example[n + 1] = example [n + 1], example[n]
        n += 2
print(example)