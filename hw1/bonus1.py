# Программа принимает на ввод 4 числа.
# Необходимо сложить первые два и отдельно вторые два.
# Разделить первую сумму на вторую.
# Выведите результат на экран

a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
c = float(input('Enter third number: '))
d = float(input('Enter fourth number: '))

first = a + b
second = c + d

result = first / second

print (result)
