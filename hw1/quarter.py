"""
    Программа принимает на ввод координату x и y точки.
    Выводит, в какой четверти системы координат лежит точка.
                ^ y
                |
            II  |    I
                |
        --------=-------->
                |         x
            III |    IV
                |
"""

x = int(input('Enter coordinate x: '))
y = int(input('Enter coordinate y: '))

if x > 0 and y > 0:
    print ('Point ', x, ':', y, ' is in the first quarter.', sep = '')
elif x < 0 and y > 0:
    print ('Point ', x, ':', y, ' is in the second quarter.', sep = '')
elif x < 0 and y < 0:
    print ('Point ', x, ':', y, ' is in the third quarter.', sep = '')
elif x > 0 and y < 0:
    print ('Point ', x, ':', y, ' is in the fourth quarter.', sep = '')
else:
    print ('Point ', x, ':', y, ' is not in any quarter.', sep = '')
