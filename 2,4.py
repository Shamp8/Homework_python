text = input("Введите текст: ")
word = []
num = 1
for el in range(text.count(' ') + 1):
    word = text.split()
    if len(str(text)) <= 10:
        print(f" {num} {word [el]}")
        num += 1
    else:
        print(f" {num} {word [el] [0:10]}")
        num += 1