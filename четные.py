#Напишите программу, ĸоторая запрашивает у пользователя ( n ) чисел и выводит ĸоличество четных и нечетных чисел.
n = int(input("Введите количество чисел: "))
#четное число
chetnoe = 0
#нечетное
nechetnoe = 0

for i in range(n):
    x = int(input("Введите любое число: "))
    if x % 2 == 0:
        chetnoe += 1
    else:
        nechetnoe += 1
print(f"количество четных чисел {chetnoe}")
print(f"количество нечетных чисел {nechetnoe}")
