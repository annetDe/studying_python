"""
    Обновить калькулятор из 1 дз.
    1. Если введены не числа, выводить соответствующее сообщение.
    2. Обрабатывать деление на 0.
"""

first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
operator = input('Enter operator (+, -, *, /, //, %, **): ')

result = 'Unknown operator.'

try:
    first_num, second_num = int(first_num), int(second_num)
except:
    print('Введены не числа')
else:
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif operator == '**':
        result = first_num ** second_num
    elif second_num == 0:
        result = 'Деление на ноль невозможно'
    elif operator == '/':
        result = first_num / second_num
    elif operator == '//':
        result = first_num // second_num
    print(result)
