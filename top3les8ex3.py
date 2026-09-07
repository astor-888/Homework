m = int(input())
n = int(input())
weights = []
for i in range(n):
    weights.append(int(input()))
weights.sort()
l = 0
r = n - 1
boats = 0
while l <= r:
    if weights[l] + weights[r] <= m:
        l = l + 1
    r = r - 1
    boats = boats + 1
print(boats)