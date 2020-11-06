"""
    Выполнить описанные действия над строкой.
"""

string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Вывести получившуюся строку.
string = string.replace(', ', ' ')
print(f'1: {string}')

# 2. Вывести индекс самой последней буквы 's' в строке.
print(f'2: {string.rfind("s")}')

# 3. Вывести количество букв 'i' в строке (регистр не имеет значения).
print(f'3: {string.lower().count("i")}')

# 4. Вывести срез строки.
#    Условие: от 'simply' до 'of' не включительно
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)
print(f'4: {string[string.find("simply"):string.find("of")]}')

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной.
#    Выведите результат.
index_half = int(len(string) // 2)
print(f'5: {string[:index_half] * 3 + string[index_half:]}')
