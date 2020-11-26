"""
    Пользователь вводит количество групп n.
    Далее вводится n строк, каждая строка начинается с названия группы,
    а затем через пробел идут элементы группы.
    1. Обработать строки и вывести на экран словарь, в котором
    ключи - это группы, а значения - списки элементов групп.
    2. Создать и вывести второй словарь, в котором
    ключи - элементы групп, а зачения - группы.
    Используйте функции!
    Например:
    [out] Введите кол-во групп:
    [in]  2
    [out] 1 группа:
    [in]  fruits apple banana mango kiwi lemon
    [out] 2 группа:
    [in]  citrus lime lemon orange
    [out] {
        'fruits': ['apple', 'banana', 'mango', 'kiwi', 'lemon'],
        'citrus': ['lime', 'lemon', 'orange']
    }
    [out] {
        'apple': ['fruits'],
        'lemon': ['citrus', 'fruits'],
        ...
    }
"""


def main():
    n = int(input('Введите количество групп: '))
    dict1 = lines_input(n)
    dict2 = swap_key_values(dict1)
    dict_print(dict1)
    dict_print(dict2)


def lines_input(n):
    lines_dict = {}
    for i in range(n):
        line_i = input(f'{i + 1} группа:').split()
        lines_dict.update({line_i[0]: line_i[1:]})
    return lines_dict


def swap_key_values(dict_):
    key_list = []
    for value in dict_.values():
        for i in value:
            if i not in key_list:
                key_list.append(i)
    value_list = list(dict_.keys())
    dict_out = {}
    for k in key_list:
        tmp = []
        for v in value_list:
            if k in dict_[v]:
                tmp.append(v)
        dict_out.update({k: tmp})
    return dict_out


def dict_print(dict_):
    print('{')
    for key, value in dict_.items():
        print(f'\t{key}:\t{value}')
    print('}')


main()
