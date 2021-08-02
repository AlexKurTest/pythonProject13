n = int(input("Количество билетов:"))
s = 0
s1 = 0
s2 = 990
s3 = 1390
for i in range(n):
    age = int(input("Возраст:"))
    if 18 > age:
        s = s + s1
    elif 18 < age < 25:
        s = s + s2
    elif 25 < age:
        s = s + s3
if n > 3:
    s = s * (1 - 0.1)
print("Стоимость билетов =", s , "руб.")