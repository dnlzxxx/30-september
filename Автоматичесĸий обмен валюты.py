value = int(input("Введите курс валюты: "))
percent = float(int(input("Введите процент: ")))
n = int(input("Введите количество дней: "))
if n <= 0:
    print("Число не может быть отрицательным!")
x = value
for i in range(n):
    x += (value/100)*percent
    print(x)