"""
    Определить, существует ли треугольник.
    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.
    * У треугольника сумма двух любых сторон должна быть больше третьей
"""

a = int(input('Enter first side of triangle: '))
b = int(input('Enter second side of triangle: '))
c = int(input('Enter third side of triangle: '))

if a + b > c and a + c > b and b + c > a:
	print ('Triangle with sides', a, b, c, 'is exists.')
else:
	print ('Triangle with sides', a, b, c, 'is not exists.')
