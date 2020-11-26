"""
    Реализовать функции, которые принимают 2 списка чисел и:
    1 функция
    Возвращает список чисел (в порядке возрастания),
    которые содержатся в первом и втором списке одновременно.
    2 функция
    Возвращает список чисел (в порядке убывания),
    которые не содержатся в первом и втором списке одновременно.
    3 функция
    Возвращает количество уникальных чисел,
    которые содержатся во втором списке, но не содержатся в первом.
"""


def main():
    list1 = input('Первый список чисел: ').split()
    list2 = input('Второй список чисел: ').split()
    print(f'1: {list_increase(list1, list2)}')
    print(f'2: {list_decrease(list1, list2)}')
    print(f'3: {list2_unique(list1, list2)}')


def list_increase(list1, list2):
    l_out = list(set(list1) & set(list2))
    l_out.sort()
    return l_out


def list_decrease(list1, list2):
    l_out = list(set(list1) ^ set(list2))
    l_out.sort(reverse=True)
    return l_out


def list2_unique(list1, list2):
    return len((set(list2) - set(list1)))


main()
