"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

s = input().strip() + ' '

count_words = 0
count_letters = 0
current_word = ''
longest_word = ''
longest_word_len = 0
for i in s:
    if i == ' ':
        if count_letters > longest_word_len:
            longest_word_len = count_letters
            longest_word = current_word
        count_words += 1
        count_letters = 0
        current_word = ''
    elif i.isalpha():
        count_letters += 1
        current_word += i

print(f'Слов в введённой строке: {count_words}')
print(f'Самое длинное слово: {longest_word} - длиной: {longest_word_len} символов.')
