"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, который не меньше размеров его ноги.
    Напишите программу, которая принимает список доступных размеров коньков и
    список размеров ног желающих.
    И выводит наибольшее количество людей,
    которые смогут покататься одновременно.
    Например:
    [in]
    [39, 38, 41, 37]
    [40, 39, 41]
    [out]
    2
"""

import re


def main():
    sizes_avail = re.findall(r'\d+', input('Список доступных размеров коньков: '))
    w_sizes_avail = [int(i) for i in sorted(sizes_avail)]
    foot_sizes = re.findall(r'\d+', input('Список размеров ног желающих: '))
    w_foot_sizes = [int(i) for i in sorted(foot_sizes)]
    count = 0
    while True:
        if not w_foot_sizes or not w_sizes_avail:
            break
        if w_foot_sizes[0] <= w_sizes_avail[0]:
            count += 1
            w_foot_sizes.pop(0)
            w_sizes_avail.pop(0)
        else:
            w_sizes_avail.pop(0)
    print(count)


main()
