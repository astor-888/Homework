import collections

pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}}
}

def get_suffix(age):
    last_digit = age % 10
    last_two = age % 100
    if last_digit == 1 and last_two != 11:
        return "год"
    elif last_digit in [2, 3, 4] and not (last_two in [12, 13, 14]):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    return pets[ID] if ID in pets else False

def pets_list():
    for pid in pets:
        pet_data = pets[pid]
        pet_name = list(pet_data.keys())[0]
        info = pet_data[pet_name]
        print(f"ID: {pid}. {info['Вид питомца']} по кличке \"{pet_name}\". "
              f"Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. "
              f"Имя владельца: {info['Имя владельца']}")

def create():
    if len(pets) == 0:
        new_id = 1
    else:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1

    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pet_info = {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}
    pets[new_id] = {name: pet_info}
    print(f"Запись с ID {new_id} создана.")

def read():
    pid = int(input("Введите ID питомца: "))
    pet = get_pet(pid)
    if pet:
        pet_name = list(pet.keys())[0]
        info = pet[pet_name]
        print(f"Это {info['Вид питомца']} по кличке \"{pet_name}\". "
              f"Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. "
              f"Имя владельца: {info['Имя владельца']}")
    else:
        print("Питомец с таким ID не найден.")

def update():
    pid = int(input("Введите ID питомца для обновления: "))
    pet = get_pet(pid)
    if pet:
        pet_name = list(pet.keys())[0]
        print("Введите новые данные (если не хотите менять, оставьте пустым и нажмите Enter):")
        new_species = input("Вид питомца: ")
        new_age_str = input("Возраст питомца: ")
        new_owner = input("Имя владельца: ")
        if new_species:
            pet[pet_name]["Вид питомца"] = new_species
        if new_age_str:
            pet[pet_name]["Возраст питомца"] = int(new_age_str)
        if new_owner:
            pet[pet_name]["Имя владельца"] = new_owner
        print(f"Запись с ID {pid} обновлена.")
    else:
        print("Питомец с таким ID не найден.")

def delete():
    pid = int(input("Введите ID питомца для удаления: "))
    if pid in pets:
        del pets[pid]
        print(f"Запись с ID {pid} удалена.")
    else:
        print("Питомец с таким ID не найден.")

command = ""
while command != "stop":
    command = input("Введите команду (create/read/update/delete/stop): ").lower()
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "stop":
        print("Работа завершена.")
    else:
        print("Неизвестная команда.")