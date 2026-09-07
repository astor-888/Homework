pets = {}

name = input("Введите имя питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

pet_info = {
    "Вид питомца": species,
    "Возраст питомца": age,
    "Имя владельца": owner
}

pets[name] = pet_info

for pet_name in pets.keys():
    inner = pets[pet_name]
    values_list = list(inner.values())
    species_out = values_list[0]
    age_out = values_list[1]
    owner_out = values_list[2]

if age_out % 10 == 1 and age_out % 100 != 11:
    year_word = "год"
elif age_out % 10 in [2, 3, 4] and not (age_out % 100 in [12, 13, 14]):
    year_word = "года"
else:
    year_word = "лет"

print(f"Это {species_out} по кличке \"{pet_name}\". Возраст питомца: {age_out} {year_word}. Имя владельца: {owner_out}")