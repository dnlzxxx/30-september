a = int(input("Введите начальный член: "))
r = int(input("Введите знаменатель: "))
n = int(input("Введите число: "))
for i in range(n):
    x = a * (r ** i)
    print(x)

