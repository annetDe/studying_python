"""
    Напишите функцию, которая приинимает текст и
    возвращает слово, которое в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    * Если таких слов несколько - приоритет у первого,
        если расположить список в алфавитном порядке.
"""

import re


def frequent_word(text):
    word_list = re.findall(r'[a-zA-Zа-яА-я]+', text)  # избавиться от punct
    # создание словаря с keys = слова, values = количество слов в тексте
    dict_ = {}
    for i in word_list:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    max_value = 0  # поиск самого частого повторения
    for value in dict_.values():
        if max_value < value:
            max_value = value
    # создание списка с самыми частыми словами
    freq_word_list = [key for key, value in dict_.items() if value == max_value]
    # новый список со словами в нижнем регистре + сортировка
    low_freq_list = [i.lower() for i in freq_word_list]
    low_freq_list.sort()
    # поиск частого слова в оригинальном списке
    for i in freq_word_list:
        if i.lower() == low_freq_list[0]:
            return i


t_1 = 'Harry is at Gryffindor, Hermione is at Gryffindor.'
assert frequent_word(t_1) == 'at'

t_2 = 'Harry is at Gryffindor, Hermione is in Gryffindor.'
assert frequent_word(t_2) == 'Gryffindor'

t_3 = 'abc, ab: abc, Bca and sqr'
assert frequent_word(t_3) == 'abc'
