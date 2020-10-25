"""
    Необходимо написать простой калькулятор, который принимает на ввод:
    первое число, второе число и оператор
    В зависимости от введенного оператора, между числами проводится определенная операция.
    Результат операции выводится на экран.
"""

first_num = float(input('Enter first number: '))
second_num = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /, //, %, **): ')

if operator == '+':
	result = first_num + second_num
	print(result)
elif operator == '-':
	result = first_num - second_num
	print(result)
elif operator == '*':
	result = first_num * second_num
	print(result)
elif operator == '/':
	result = first_num / second_num
	print(result)
elif operator == '//':
	result = first_num // second_num
	print(result)
elif operator == '**':
	result = first_num ** second_num
	print(result)
else:
	print('Unknown operator.')

# если не анализировать введённый оператор и считать, что он всегда будет валидным,
# тогда можно строку print(result) написать один раз после выполнения блока if-else
