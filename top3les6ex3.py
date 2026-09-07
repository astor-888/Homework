A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A % 2 == 0:
    num = A
else:
    num = A + 1

while num <= B:
    print(num, end=" ")
    num = num + 2

print()