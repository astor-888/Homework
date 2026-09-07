N = int(input("Введите количество чисел: "))
count = 0
i = 0
while i < N:
    num = int(input())
    if num == 0:
        count = count + 1
    i = i + 1
print("Количество нулей:", count)