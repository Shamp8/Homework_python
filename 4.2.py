# Список со значениями, где каждый больше предыдущего

in_list = [10, 12, 62, 3, 11, 10, 3, 13, 89, 1, 81, 33, 34]
res_list = [number for i, number in enumerate(in_list) if i > 0 and in_list[i] > in_list[i - 1]]
print(res_list)