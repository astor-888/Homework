N = int(input())
line = input()
parts = line.split()
arr = []
for p in parts:
    arr.append(int(p))

if len(arr) > 0:
    last = arr[-1]
    i = len(arr) - 1
    while i > 0:
        arr[i] = arr[i-1]
        i = i - 1
    arr[0] = last

for num in arr:
    print(num, end=" ")
print()