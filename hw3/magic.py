"""
    Магическое число.
    При запуске программы генерируется число, которое нужно угадать.
    Подсказки: больше или меньше.
    Программа в бесконечном цикле.
    После отгадывания появляется результат: само число, количество попыток,
        а так же вопрос: "Continue? (y/n)"
    * Для генерации случайного числа можно воспользоваться
        функцией random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
"""

import random

c = 'y'
while c == 'y':
    a = int(input('Задайте минимальное число: '))
    b = int(input('Задайте максимальное число: '))

    random_number = random.randint(a, b)  # случайное число от 1 до 100

    user_number = 0
    i = 0
    while user_number != random_number:
        user_number = int(input('Введи догадку: '))
        i += 1
        if user_number < random_number:
            print('Загаданное число больше')
        elif user_number > random_number:
            print('Загаданное число меньше')
        else:
            print('Bingo:', random_number)
            print('Число отгадано за', i, 'попыток.')
    print('Continue? (y/n)')
    c = input()
