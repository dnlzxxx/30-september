n = int(input("Введите количество вводимых чисел: "))
s = 0
u = 1
sr = 0
for i in range(n):
    x = int(input("Введите число: "))
    s += x
    u *= x
    sr = s/n
print(f"Сумма равна {s}")
print(f"Произведение равно {u}")
print(f"Среднее арифметическое равно {sr}")