l = int(input("Введите число до 1000"))
if l >= 1000:
    print("ДО 1000!!!!1")
for i in range(10, l + 1):
    n3 = i//100
    n2 = i//10%10
    n1 = i%10
    if n2 != n1 and n2 != n3 and n3 != n1:
        if n3 == 0:
            print(f"{n2} {n1}")
            print(f"{n1} {n2}")
        else:
            print(f" {n3} {n2} {n1}")
            print(f" {n3} {n1} {n2}")
            print(f" {n2} {n3} {n1}")
            print(f" {n2} {n1} {n3}")
            print(f" {n1} {n3} {n2}")
