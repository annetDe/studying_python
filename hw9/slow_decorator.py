"""
    Напишите декоратор, который будет замедлять выполнение функции на 5 секунд.
    Если функция выполняется более 10 секунд (с учетом замедления), то
    дополнительно выводить сообщение f'{func.__name__} - very slow function'
"""

import time


def slowdown(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(5)
        result = func(*args, **kwargs)
        end = time.time() - start
        if end > 10:
            print(f'{func.__name__} - very slow function')
        return result
    return wrapper


@slowdown
def create_list():
    return [i for i in range(10**5)]


def main():
    create_list()


main()
