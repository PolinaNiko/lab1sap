s = input("Введите строку:")
l = len(s)
str = s
s = str.split()
print("Самое длинное слово:", max(s, key = len))
print(str.swapcase())
k = 0
for i in str:
    if i.isdigit():
        k +=int(i)
print("Сумма цифр =", k)
