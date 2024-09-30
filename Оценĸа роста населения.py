value = int(input("Введите количество населения: "))
percent = float(input("Введите процентный прирост: "))
n = int(input("Введите количество лет: "))
if n <= 0:
    print("Число не может быть отрицательным или равно 0!")
x = value
for i in range(n):
    x += (value/100)*percent
    print(round(x))