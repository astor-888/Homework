N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

reversed_arr = []
for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])

for num in reversed_arr:
    print(num, end=" ")
print()