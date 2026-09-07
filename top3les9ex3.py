line = input()
parts = line.split()
seen = set()
for p in parts:
    num = int(p)
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)