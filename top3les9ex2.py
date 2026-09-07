line1 = input()
parts1 = line1.split()
line2 = input()
parts2 = line2.split()

set1 = set()
for p in parts1:
    set1.add(int(p))

set2 = set()
for p in parts2:
    set2.add(int(p))

common = set1 & set2
print(len(common))