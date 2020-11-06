"""
    Вводится строка.
    (!!! 1 пункт не изменяет строку, а 2 и 3 - изменяют !!!)
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f, format либо %)
"""

string = input().strip()

count_u = count_l = 0

for i in string:
    if i.isupper():
        count_u += 1
    elif i.islower():
        count_l += 1

print(f'Исходная строка: {string}')

template_1 = '1: {}.'

if count_u > count_l:
    print(template_1.format(string.upper()))
elif count_u < count_l:
    print(template_1.format(string.lower()))
else:
    print(template_1.format(string.swapcase()))

if string.istitle():
    string = 'done. ' + string
else:
    string = 'draft: ' + string[5:]
print(f'2: {string}')

if len(string) > 20:
    string = string[:20]
else:
    string = string.ljust(20, '@')
print(f'3: {string}')
