"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
        Программа выводит сообщение:
        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********
"""
import string


def main():
    phone = input_phone()
    email = input_email()
    password = input_password()
    print(
        '\nПоздравляем с успешной регистрацией!\n'
        f'Ваш номер телефона: {phone}\n'
        f'Ваш email: {email}\n'
        f'Ваш пароль: {"*" * len(password)}\n'
    )


def input_phone():
    phone_number = input('Введите номер телефона: ').strip()

    result_number = ''
    for i in phone_number:
        if i.isdecimal():
            result_number += i

    result_number = '380' + result_number[-9:]

    if len(result_number) != 12:
        return input_phone()
    return result_number


def input_email():
    email = input('Введите email: ').strip()

    if len(email) < 6 or email.count('@') != 1:
        return input_email()
    return email


def input_password():
    password = input('Введите пароль: ').strip()

    is_space, one_upper, one_lower, one_digit, one_punct = 0, 0, 0, 0, 0
    for i in password:
        if i.isspace():
            is_space = 1
        elif i in string.ascii_uppercase:
            one_upper = 1
        elif i in string.ascii_lowercase:
            one_lower = 1
        elif i in string.digits:
            one_digit = 1
        elif i in string.punctuation:
            one_punct = 1

    if len(password) < 8 or is_space or one_upper == 0 or one_lower == 0 or one_digit == 0 or one_punct == 0:
        return input_password()
    return confirm_password(password)


def confirm_password(password):
    conf_password = input('Подтвердите пароль: ').strip()
    if conf_password != password:
        return input_password()
    return password


main()
