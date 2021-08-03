number = int(input("Введите новое значение рейтинга: "))
rating = [9,8,5,3]
n = rating.count(rating)
for element in rating:
    if n > 0:
        i = my_list.index(number)
        rating.insert(i+n, number)
        break
    else:
        if number > element:
            k =rating.index(element)
            rating.insert(k, number)
            break
        elif number < rating[len(rating) - 1]:
            rating.append(number)
print(rating)