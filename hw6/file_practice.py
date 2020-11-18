"""
    Выполните все пункты.
    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files'
# Файл должен заканчиваться пустой строкой

# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран

# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее количество,
# иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое

file_name = 'files/file_practice.txt'
# 1
with open(file_name, 'w+') as file:
    file.write('Starting practice with files\n')
    # 2
    file.seek(0)
    print(file.read())
    file.seek(0)
    print(file.read(5))

# 3
with open(file_name, 'a+') as file:
    with open('files/text.txt', 'r') as file_text:
        data = file_text.read()
        if data.count('i') > data.count('e'):
            data_new = data.replace('i', 'e')
        else:
            data_new = data.replace('e', 'i')
        file.write(data_new)
    # 4
    file.write('\n*some pasted text*')
    if file.tell() % 2 == 0:
        file.write('\nthe end')
    else:
        file.write('\nbye')
    file.seek(0)
    print(file.read())
