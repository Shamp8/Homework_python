time=int(input("Задайте секунды: "))
hour = time//3600
min = time%3600//60
sec = time%3600%60
print(f"время: {hour}:{min}:{sec}")


