"""
    Напишите функцию, которая принимает словарь,
    меняет местами ключи и значения и возвращает его.
    Покройте функцию несколькими тестами.
    Пример:
    a = {'key': 'value', 'd': 1234}
    b = swap_items(a)
    print(b)
    {'value': 'key', 1234: 'd'}
    * пропускайте пары, в которых значение не может быть ключем
    ** ключем словаря может быть только не изменяемый объект,
        а точнее тот, который можно захешировать функцией hash()
"""


def swap_items(dict_):
    key_list = list(dict_.values())
    value_list = list(dict_.keys())
    dict_out = {}
    for i in range(len(key_list)):
        try:
            dict_out.update({key_list[i]: value_list[i]})
        except TypeError:
            continue
    return dict_out


t_1 = {'key': 'value', 'd': 1234}
assert swap_items(t_1) == {'value': 'key', 1234: 'd'}

t_2 = {1: (2, 3, 4), '2': 234}
assert swap_items(t_2) == {(2, 3, 4): 1, 234: '2'}

t_3 = {1: [2, 3, 4], '2': 234}
assert swap_items(t_3) == {234: '2'}

t_4 = {1: {2, 3, 4}, '2': 234}
assert swap_items(t_4) == {234: '2'}

t_5 = {1: {2: 'second', 3: 'third'}, '2': 234}
assert swap_items(t_5) == {234: '2'}
