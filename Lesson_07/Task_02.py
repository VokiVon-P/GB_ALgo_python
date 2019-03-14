__author__ = 'Павел Новиков (aka VokiVon)'

import random

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
"""

# сделаны переменными для возможности переопределения в модулях
size = 10
min_item = 0    # 0 включительно
max_item = 49   # 50 не включая


def gen_array():
    """
    :return: сгенерированный массив по заданным параметрам констант
    """
    return [random.uniform(min_item, max_item) for _ in range(size)]




def merge_arrays(arr_, start1, end1, start2, end2):
    """
    Слияние двух массивов - предполагается что элементы их идут друг за другом: часть 1 затем часть 2
    :param arr_: массив
    :param start1:  начало части 1
    :param end1:    конец части 1
    :param start2:  начало части 2 ( следующий элемент за концом части 1 )
    :param end2:    конец части 2
    :return: отсортированный массив
    """

    counter_left = start1
    counter_right = start2

    idx = 0
    res_arr = list()

    # сравниваем элементы двух списков
    while (counter_left <= end1) and (counter_right <= end2):
        if arr_[counter_left] < arr_[counter_right]:
            res_arr.append(arr_[counter_left])
            counter_left += 1
        else:
            res_arr.append(arr_[counter_right])
            counter_right += 1

    while counter_left <= end1:
        res_arr.append(arr_[counter_left])
        counter_left += 1

    while counter_right <= end2:
        res_arr.append(arr_[counter_right])
        counter_right += 1

    for i, item in enumerate(res_arr):
        arr_[start1+i] = item

    return arr_




def merge_sort(arr_, first, last):
    """
    Рекурсивное разбитие массива на подмассивы и сортировка их через слияние
    :param arr_:
    :param first:
    :param last:
    :return:
    """

    if first >= last:
        return

    middle = (last + first) // 2
    merge_sort(arr_, first, middle)
    merge_sort(arr_, middle+1, last)
    return merge_arrays(arr_, first, middle, middle + 1, last)



array = gen_array()
print(array)
print(merge_sort(array, 0, len(array)-1))


