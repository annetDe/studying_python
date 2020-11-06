"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.
    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""

phone_number = input().strip()

result_number = ''
for i in phone_number:
    if i.isdecimal():
        result_number += i

result_number = '38' + result_number[result_number.find('0'):]

if len(result_number) == 12:
    print(result_number)
else:
    print('Недостаточно цифр в номере. Повторите ввод.')
