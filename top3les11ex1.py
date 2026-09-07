def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

n = int(input())
fact_n = factorial(n)
print(fact_n)

factorial_list = []
for i in range(fact_n, 0, -1):
    factorial_list.append(factorial(i))

print(factorial_list)