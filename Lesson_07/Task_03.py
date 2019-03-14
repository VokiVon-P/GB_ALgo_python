__author__ = 'Павел Новиков (aka VokiVon)'

import random

"""
3. Массив размером 2m + 1, 
где m – натуральное число, 
заполнен случайным образом. 
Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. 
Задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""

# сделаны переменными для возможности переопределения в модулях
size_m = 3
min_item = -100  # -100 включительно
max_item = 100    # 100 не включая

def gen_array():
    """
    :return: сгенерированный массив по заданным параметрам констант
    """
    return [random.randint(min_item, max_item) for _ in range(size_m*2 + 1)]


def quick_median(arr_):
    """
    Почти быстрая сортировка, только находим медиану
    :param arr_: сортируемый массив
    :return: медиана
    """

    # проверим на возможность найти медиану
    if len(arr_) % 2 == 1:
        return select_median(arr_, len(arr_) / 2)



def select_median(arr_, idx):
    """
    Выбираем idx-тый элемент в массиве arr_ (с нулевой базой)
    :param arr_: массив
    :param idx: индекс
    :return: idx-тый элемент arr_
    """
    if len(arr_) == 1:
        return arr_[0]

    pivot = random.choice(arr_)

    small = [item for item in arr_ if item < pivot]
    large = [item for item in arr_ if item > pivot]
    pivots = [item for item in arr_ if item == pivot]

    if idx < len(small):
        return select_median(small, idx)
    elif idx < len(small) + len(pivots):
        # Yes -  мы нашли медиану
        return pivots[0]
    else:
        return select_median(large, idx - len(small) - len(pivots))


array = gen_array()
print(array)
print(quick_median(array))
print(array)
