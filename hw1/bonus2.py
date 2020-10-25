# Программа принимает на ввод 3 значения.
# Если все значения – числа, тогда вывести самое большое и самое маленькое из них,
# иначе вывести все значения.

a = (input('Enter first number: '))
b = (input('Enter second number: '))
c = (input('Enter third number: '))

if a.isdigit() and b.isdigit() and c.isdigit():
	if a >= b and a >= c and b >= c:
		print('Max number is', a, 'and min number is', c)
	elif a >= b and a >= c and c > b:
		print('Max number is', a, 'and min number is', b)
	elif b > a and b >= c and a >= c:
		print('Max number is', b, 'and min number is', c)
	elif b > a and b >= c and c > a:
		print('Max number is', b, 'and min number is', a)
	elif c > a and c > b and a >= b:
		print('Max number is', c, 'and min number is', b)
	else:
		print('Max number is', c, 'and min number is', a)
else:
	print(a, b, c)
