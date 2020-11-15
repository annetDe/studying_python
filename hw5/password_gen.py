"""
Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1 Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2 Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3 Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая,
    1 цифра и 1 спец-символ, длина от 8 до 16 символов)
(для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из
    последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного
    пароля от 8 до 16 символов)
    Дополнительно (не влияет на оценку):
    1 Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2 Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться
        пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""

import random
import string


def main():
    var = 0
    while var not in ('1', '2', '3'):
        var = input('Выберите вариант генерируемого пароля (1 - простой, 2 - средний, 3 - сложный): ')
    if var == '1':
        print(gen_simple_pass())
    elif var == '2':
        print(gen_mid_pass())
    elif var == '3':
        print(gen_complex_pass())


def gen_simple_pass():  # только буквы в нижнем регистре, 8 символов
    return ''.join(random.sample(string.ascii_lowercase, 8))


def gen_mid_pass():  # любые буквы и цифры, 8 символов
    tmp = string.ascii_letters + string.digits
    return ''.join(random.sample(tmp, 8))


def gen_complex_pass():  # минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов
    pass_len = random.randint(8, 16)
    tmp = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    while True:
        password = ''.join(random.sample(tmp, pass_len))
        one_upper, one_lower, one_digit, one_punct = 0, 0, 0, 0
        for i in password:
            if i in string.ascii_uppercase:
                one_upper = 1
            elif i in string.ascii_lowercase:
                one_lower = 1
            elif i in string.digits:
                one_digit = 1
            elif i in string.punctuation:
                one_punct = 1
        if one_upper and one_lower and one_digit and one_punct:
            break
    return password


main()
