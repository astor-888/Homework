number = int(input("Введите любое пятизначное число: "))
units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = number // 10000
result = (tens ** units * hundreds) / (ten_thousands - thousands)
print("result:", result)
