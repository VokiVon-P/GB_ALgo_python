__author__ = 'Павел Новиков (aka VokiVon)'

"""
1. Проанализировать скорость и сложность одного любого алгоритма, 
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import random
import cProfile

def get_arr(size_):
    min_item = 0
    max_item = 10
    size = size_
    return [random.randint(min_item, max_item) for _ in range(size)]


def test_func(func):
    test_list = [4, 2, 8, 7, 2, 2, 0, 4, 2, 8, 2, 5, 10, 2, 1, 2, 2, 7, 9, 5]
    res = func(test_list)
    assert res[0] == 8
    assert res[1] == 2
    print(f"Test = OK")


def freq_01(arr_):
# создадим словарь где ключ - значение элемента массива,
# а значение элемента словаря - частота встречи
    dict_freq = {}
    freq = 1
    out_item = None

    for i in arr_:
        if i in dict_freq:
            dict_freq[i] += 1
        else:
            dict_freq[i] = 1
        # проверка на мах - если бы можно было использовать max, сделал бы по другому
        if dict_freq[i] > freq:
            freq = dict_freq[i]
            out_item = i

    return (freq, out_item)

def freq_02(arr_):
    """
    Используем встроенную фукцию count
    :param arr_: массив для обратотки
    :return: кортеж 1 элемент - частота, 2 элемент - значение
    """

    freq = 1
    out_item = None

    for i in arr_:
        temp = arr_.count(i)
        if temp >= freq:
            freq = temp
            out_item = i

    return (freq, out_item)


#test_func(freq_02)


def test_func_01(size):
    freq_01(get_arr(size))
#  "Test_01.test_func_01(20)"
# 100 loops, best of 3: 31.9 usec per loop
#  "Test_01.test_func_01(30)"
# 100 loops, best of 3: 51.5 usec per loop
#  "Test_01.test_func_01(40)"
# 100 loops, best of 3: 58.9 usec per loop
# cProfile.run("test_func_01(200000)")
# 1    0.019    0.019    0.019    0.019 Test_01.py:27(freq_01) - 100000
# 1    0.053    0.053    0.053    0.053 Test_01.py:27(freq_01) - 200000
# 1    0.076    0.076    0.076    0.076 Test_01.py:27(freq_01) - 300000





def test_func_02(size):
    freq_02(get_arr(size))
#  "Test_01.test_func_02(20)"
# 100 loops, best of 3: 31.8 usec per loop
#  "Test_01.test_func_02(30)"
# 100 loops, best of 3: 52.3 usec per loop
#  "Test_01.test_func_02(40)"
# 100 loops, best of 3: 94.3 usec per loop
cProfile.run("test_func_02(100000)")
# 1    0.124    0.124  150.130  150.130 Test_01.py:46(freq_02) - 100000
# дальше смысла нет тестировать - итак еле дождался ))

"""
Вывод:
По результатам моего тестирования алгоритм 01 со словарем оказался гораздо быстрее и оптимальнее
"""


def print_res(res):
    itm = res[1]
    fr = res[0]

    if itm is not None:
        print(f'Число {itm} встречается наибольшее количество ({fr}) раз!')
    else:
        print('Элементы не повторяются')


frq_list = get_arr(20)
print(frq_list)
print_res(freq_01(frq_list))
print_res(freq_02(frq_list))



