import random
from datetime import datetime

# Исходные данные:
# Предметы с оценками
school_attestat = {
    "Сложение на калькуляторе": 5,
    "Физика в вакууме": 4,
    "Русский язык на татарском": 2,
    "Бобриный язык": 0,
    "Химия с Хайзенбергом": 4,
    "Зельеварение": 7,
    "Анжуманя и подтягиня": 5,
    "Бег с яйцом в ложке": 88,
    "Информатика и ИКТ, МРТ, МВД, ФСБ": 44,
    "История Древнего Рима": 3,
    "Слепое чтение": 4,
    "Труды Карла Маркса": 3,
    "Тяжелая музыка": 5,
    "Знание состава BTS": 2
}

# Актер вестерна 60-х
info = ("Чарльз Бронсон", "3 ноября 1921 г.")

# Список из самых популярных имени и фамилии в Нижнем Новгороде согласно сайту topnamesinrussia.tilda.ws
names = ["Иван", "Сергей", "Александр", "Дмитрий", "Алексей", "Андрей", "Максим", "Михаил", "Евгений", "Владимир"]
surnames = ["Иванов", "Смирнов", "Кузнецов", "Петров", "Белов", "Волков", "Соколов", "Морозов"]
unique_names = []
for i in range(0, len(names)):
    rname = random.choice(names)
    rsurname = random.choice(surnames)
    unique_names.append(rname)
    unique_names.append(rsurname)

# Имя моего тамандуа
domestic_tamandua = "Боевой вертолет"

# Действия:
# 1. Средняя оценка в аттестате
summa = sum(school_attestat.values())
kolvo = len(school_attestat)
sredn_znach = round(summa / kolvo, 1)
print('\n', "Задание 1. Средняя оценка в аттестате", '\n', sredn_znach)

# 2. Вывод уникальных имен
print('\n', "Задание 2. Вывод уникальных имен")
spisok = []
for i in range(0, len(names)):
    spisok.append(random.choice(names))
    print(random.choice(names), random.choice(surnames))
# print(spisok)

# 3. Общая длина всех названий предметов (с исключением пробелов и запятых)
print('\n', "Задание 3. Общая длина названий предметов в аттестате")
length = 0
for i in school_attestat:
    length += len(i.replace(" ", "").replace(",", ""))
print("Общая длина: ", length)

# 4. Уникальные буквы в названиях предметов
print('\n', "Задание 4. Уникальные буквы в названиях предметов")
uniq = []
attestlist = list(school_attestat)
for i in range(len(attestlist)):
    for j in attestlist[i]:
        uniq.append(j)
uniq = set(uniq)
print(uniq)

# 5. Имя тамандуа в бинарном виде
print('\n', "Задание 5. Имя тамандуа в бмнарном виде")
string = " "
for i in domestic_tamandua:
    char_to_ascii = ord(i)
    char_to_binar = format(char_to_ascii, "08b")
    string += char_to_binar
print(string)

# 6. Количество дней от даты рождения актера до текущей
print('\n', "Задание 6. Количество дней от даты рождения актера до текущей")
now = datetime.now()
actor_date = datetime(1921, 11, 3)
difference = now - actor_date
print(difference, '\n')

# 7. FIFO очередь с добавлением стройматериалов до команды "СТОП"
print('\n', "Задание 7. FIFO очередь с добавлением стройматериалов до команды 'СТОП'")


def FIFO():
    import queue
    materials = queue.Queue()
    print("Введите СТОП, чтобы завершить добавление материалов")

    def add_material(materials):
        item = input("Добавьте материал: ")
        if item == 'СТОП':
            while materials.empty() == False:
                print(materials.get())
        else:
            materials.put(item)
            add_material(materials)

    add_material(materials)


FIFO()

# 8. Император Китая
print('\n', "Задание 8. Китайский император династии Чжоу")
s = sorted(spisok)
print(s)
imperator = 'Хуэй-ван'

# Вычисление номера китайского императора
number = (3 + 11 ** 2 + 1921) % 39 + 1
# print(number)
# 18 | Хуэй-ван

index = input("Введите индекс: ")

try:
    index = int(index)

except ValueError:
    print("Неверный индекс")

if index >= 0 and index < len(s):
    s[index] = imperator

print("Сдаем только славянам с именами:", s)

# 9. Список странных названий населенных пунктов
print('\n', "Задание 9. Вам предоставляется возможность переименовать населенный пункт")
cities = ["Дно", "Ломки", "Ширяево", "Хомяки", "Лысая Балда",
          "Чуваки", "Свиновье", "Засосная", "Вобля"]

print('\n', cities)
cities.remove(str(input("Выберите населенный пункт, который хотите переименовать: ")))

city = 'Конец'
num_in = int(input('Введите индекс, в который хотите поместить новый населенный пункт: '))
cities.insert(num_in, city)

print('\n', "Поздравляю, Вы переименовали населенный пункт...")
print(cities)
