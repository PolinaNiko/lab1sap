n = int(input("Введите натуральное число:"))
s = []
for i in range (1,n+1):
    if n % i == 0:
        s.append(i)
print("Делители:", s)
print("Максимальный:", max(s))
print("Минимальный:", min(s))