"""
    Дан файл с текстом (text.txt).
    Создать новый файл (edited_text.txt), каждая строка которого получается из
    соответствующей строки исходного файла с обратным порядком слов, причем
    первое слово с заглавной буквы, а все остальные со строчной.
    Например 1 файл содержит:
    Hello world
    How are you
    Тогда второй файл будет содержать:
    World hello
    You are how
"""

import string

with open('text.txt', 'r') as in_f:
    with open('edited_text.txt', 'w') as out_f:
        for line in in_f.readlines():
            txt_list = line.lower().split()  # список из слов текущей строки
            punc_list, r_txt_list = [], []
            for word in txt_list:
                # формирование списка позиции знаков пунктуации
                if word[-1] in string.punctuation:
                    punc_list.append(txt_list.index(word))
                    word = word[:-1]  # удалить последний символ в слове
                r_txt_list.append(word)  # в список добавить слово
            r_txt_list.reverse()  # реверс списка слов
            for i in punc_list:
                r_txt_list[i] += txt_list[i][-1]
            new_line = ' '.join(r_txt_list).capitalize() + '\n'
            out_f.write(str(new_line))
