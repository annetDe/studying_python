import random

# 1. Создайте переменную x, которая равняется 2 в степени 3
x = 2 ** 3

# 2. Прибавьте к x 3
x += 3

# 3. Сгенерируйте список num_list длиной x, из случайных чисел в диапазоне от 1 до x
num_list = [random.randint(1, x) for i in range(x)]

# 4. Выведите на экран числа из списка num_list в обратном порядке
#    (от последнего до первого элемента) через пробел
rev_num_list = list(reversed(num_list))
for i in rev_num_list:
    print(i, end=' ')
print()

# 5. Вставьте в средину списка число 11.
num_list.insert(len(num_list) // 2, 11)

# 6. Запишите в файл list_info.txt строчки
#    - количество элементом списка
#    - количество уникальных элементов списка
#    - самое маленькое число списка
#    - сумму чисел списка кратных 3
with open('list_info.txt', 'w+') as file:
    file.write(str(len(num_list)) + '\n')
    file.write(str(len(set(num_list))) + '\n')
    file.write(str(min(num_list)) + '\n')
    sum3 = 0
    for i in num_list:
        if i % 3 == 0:
            sum3 += i
    file.write(str(sum3) + '\n')

# 7. Создайте список countries_info из 3 словарей c ключами
#    'country', 'population', 'cities' и заполните их любыми значениями
#    ('country' - строка, 'population' - число, 'cities' - список строк)
countries_info = [
    {
        'country': 'Ukraine',
        'population': 41234567,
        'cities': ['Kyiv', 'Odessa', 'Lviv']
    },
    {
        'country': 'England',
        'population': 34568976,
        'cities': ['Something', 'Another', 'Again']
    },
    {
        'country': 'Spain',
        'population': 76532901,
        'cities': ['After', 'Before', 'KillMePlease']
    }
]

# 8. Отсортируйте в каждом словаре cities по длине строк в порядке убывания
print(sorted(countries_info, key=lambda data: len(data['cities'])))

# 9. Отсортируйте список словарей countries_info
#    по ключу 'population' в порядке возрастания
print(sorted(countries_info, key=lambda data: data['population']))

# 10. Напишите функцию create_country_info, которая принимает 3 параметра
#     country, population и cities
#     и возвращает словарь типа
#     {'country': 'USA', 'population': 123, 'cities': ['New York', 'Los Angeles', 'Portland']}
def create_country_info(country, population, cities):
    d = {
        'country': country,
        'population': population,
        'cities': cities
    }
    return d

# 11. Создайте словарь с помощью функции create_country_info
#     и вставьте его в начало списка countries_info
d = create_country_info('Country', 6543280, ['one', 'two', 'three'])
countries_info.insert(0, d)

# 12. Запуште код в репозиторий (существующий либо новый),
#     ссылку на файл прикрепите к 10 дз
