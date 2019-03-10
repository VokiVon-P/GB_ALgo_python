__author__ = 'Павел Новиков (aka VokiVon)'
"""
Модуль для генерации массива для всех заданий
"""
import random
import sys

# сделаны переменными для возможности переопределения в модулях
size = 20
min_item = -100
max_item = 100

# глобальная служебная переменная для расчета занимаемой памяти
mem_size_counter = 0


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

# раздел для рассчета размера занимаемой памяти

def ext_show_size(x_, show_info=False):
    """
    Функция-замыкание для подсчета количества занимаемой памяти
    с выводом расщиренной информации по каждой итерации
    :param x_: объект
    :param show_info: показывать ли отладочную инфо
    :return: кол-во памяти занимаемой объектом
    """
    arr_size = []

    def show_size(x, level=0):
        mem_size = sys.getsizeof(x)
        arr_size.append(mem_size)

        if show_info:
            print('\t' * level, f'type={type(x)}, size={mem_size}, obj={x}')

        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    show_size(key, level + 1)
                    show_size(value, level + 1)
            elif not isinstance(x, str):
                for item in x:
                    show_size(item, level + 1)

        if show_info:
            print('\t' * level, f'Размер={sum(arr_size)} содержание = {arr_size}')

        return sum(arr_size)

    return show_size(x_)


def global_size_inc(x, level=0):
    """
    Функция для увеличения глобального счетчика количества занимаемой памяти
    ничего не возвращает
    :param x: объект
    :param level: уровень вложенности
    """
    global mem_size_counter
    mem_size_counter += sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                global_size_inc(key, level + 1)
                global_size_inc(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                global_size_inc(item, level + 1)


def doble_check(x, show_info=False):
    """
    Проверка с помощью вызова двух методов расчета занимаемой памяти ))
    :param x: объект
    :param show_info: показывать ли отладочную инфо
    :return: колво занимаемой объектом памяти
    """
    global_size_inc(x)
    return ext_show_size(x, show_info)


if __name__ == "__main__":
    pass
