"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) телефоны владельцев,
    чьи имена начинаются на букву "м" либо заканчиваются на "а"
    (регистр не имеет значения).
    Перед записью в файл привести номер к формату +380501234567.
"""

import re

with open('files/phone_book.txt', 'r') as f:
    data = f.read()
    names = re.findall(r'[a-zA-Zа-яА-Я]+', data)
    f.seek(0)
    phones = []
    data_lines = f.readlines()
    for line in data_lines:
        tmp = ''.join(re.findall(r'[\d]+', line))
        tmp = '+380' + tmp[-9:]
        phones.append(tmp)

with open('files/edited_phone_book.txt', 'w') as file:
    for i in range(len(names)):
        if names[i][0].lower() == 'м' or names[i][-1].lower() == 'а':
            file.write(names[i] + '\t' + phones[i] + '\n')
