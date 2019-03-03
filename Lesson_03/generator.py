__author__ = 'Павел Новиков (aka VokiVon)'
"""
Модуль для генерации массива для всех заданий
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100


def gen_array():
    """
    :return: сгенерированный массив по заданным параметрам констант
    """
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
