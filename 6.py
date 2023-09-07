my_tuple = (1, -2, 3, 4, -5, 6)
my_list = list(my_tuple)
for i in my_list:
    if i < 0:
        my_list.remove(i)
        break
my_tuple = tuple(my_list)
print("Кортеж без первого отрицательного числа:", my_tuple)