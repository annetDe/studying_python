"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    ticket_num = str(ticket_num)
    mid = int(len(ticket_num) / 2)
    first = 0
    second = 0
    for i in ticket_num[:mid]:
        first += int(i)
    for i in ticket_num[mid:]:
        second += int(i)
    if first == second:
        return True
    else:
        return False


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
