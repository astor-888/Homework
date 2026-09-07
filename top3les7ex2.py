s = input("Введите строку: ")
result = ""
i = 0

while i < len(s):
    if s[i] == " ":
        result = result + " "
        while i < len(s) and s[i] == " ":
            i = i + 1
    else:
        result = result + s[i]
        i = i + 1

print(result)