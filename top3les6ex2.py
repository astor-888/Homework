import math

X = int(input("Введите число X: "))
count = 0
d = 1
limit = int(math.sqrt(X))

while d <= limit:
    if X % d == 0:
        if d == X // d:
            count = count + 1
        else:
            count = count + 2
    d = d + 1

print("Количество делителей:", count)