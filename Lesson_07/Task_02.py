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
    # return [random.uniform(min_item, max_item) for _ in range(size)]
    arr_ = [37.136359214314595, 34.41621511169794, 30.42571573354757, 27.774907263395654, 21.2641191518764, 20.395197995460432, 14.59299121806877, 5.598487776086833, 2.687076495847309, 1.0163188945189097]
    random.shuffle(arr_)
    return arr_



def bubble_sort_reverse(arr_):
    """
    Сортировка пузырьком, как на уроке
    :param arr_: сортируемый массив
    :return: отсортированный массив
    """
    n = 1
    while n < len(arr_):
        # на уроке стояла 1, заменил на n, т.к. при каждом проходе макс элемент уже на месте
        for i in range(len(arr_) - n):  # заменил на n
            if arr_[i] < arr_[i + 1]:   # изменил знак сравнения, чтобы всплывал минимальный элемент
                arr_[i], arr_[i + 1] = arr_[i + 1], arr_[i]
        n += 1

        # print(arr_)
    return arr_


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

    if (last - first) <= 1:
        return

    middle = (last + first) // 2
    merge_sort(arr_, first, middle)
    merge_sort(arr_, middle+1, last)
    return merge_arrays(arr_, first, middle, middle + 1, last)


array = gen_array()
print(array)
print(bubble_sort_reverse(array))

array = gen_array()
print(array)
print(merge_sort(array, 0, len(array)-1))


