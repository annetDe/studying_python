"""
    Даны 3 целых числа.
    1. Найти сумму тех чисел, которые делятся на 5, иначе вывести сообщение.
    2. Найти количество положительных чисел.
    3. Найти количество отрицательных чисел.
    4. Найти сумму 2х найбольших чисел.

    Вывести сообщение типа:

    Числа: -10, 4, 21
    1. -10
    2. 2
    3. 1
    4. 25
"""

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

sum_5 = 0

sum_5 += a if a % 5 == 0 else 0
sum_5 += b if b % 5 == 0 else 0
sum_5 += c if c % 5 == 0 else 0

if sum_5 == 0:
    print('ни одно из чисел не делится на 5 без остатка')
else:
    print(sum_5)

pos = 0

pos += 1 if a > 0 else 0
pos += 1 if b > 0 else 0
pos += 1 if c > 0 else 0

print(pos)

neg = 0

neg += 1 if a < 0 else 0
neg += 1 if b < 0 else 0
neg += 1 if c < 0 else 0

print(neg)

if a <= b and a <= c:
    print(b + c)
elif b <= a and b <= c:
    print(a + c)
else:
    print(a + b)
