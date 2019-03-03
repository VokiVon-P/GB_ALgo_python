__author__ = 'Павел Новиков (aka VokiVon)'
"""
Модуль для генерации массива для всех заданий
"""
import random

# сделаны переменными для возможности переопределения в модулях
size = 20
min_item = -100
max_item = 100


def gen_array():
    """
    :return: сгенерированный массив по заданным параметрам констант
    """
    return [random.randint(min_item, max_item) for _ in range(size)]


def gen_matrix():
    """
    :return: сгенерированную матрицу по заданным параметрам констант
    """
    return [gen_array() for _ in range(size)]


# if __name__ == "__main__":
