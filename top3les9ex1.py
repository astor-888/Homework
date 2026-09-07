N = int(input())
line = input()
parts = line.split()
unique_numbers = set()
for p in parts:
    unique_numbers.add(int(p))
print(len(unique_numbers))