"""
    Дано число от 1 до 999.
    1. Найти сумму цифр числа. (для 2-знач числа - lesson1/3_practice_operators.py)
    2. Вывести, в каком порядке расположены цифры (возрастания/убывания/в разброс)
"""

number = int(input())

if 1 <= number < 10:
    print(number)
elif 10 <= number < 100:
    d = number // 10
    u = number % 10
    print(d + u)
    if d > u:
        print('убывание')
    elif d < u:
        print('возрастание')
    else:
        print('равны')
elif 100 <= number < 1000:
    h = number // 100
    d = number % 100 // 10
    u = number % 10
    print(h + d + u)
    if h == d == u:
        print('равны')
    elif h >= d >= u:
        print('убывание')
    elif h <= d <= u:
        print('возрастание')
    else:
        print('в разброс')
else:
    print('Введено число вне диапазона 1 - 999')
