__author__ = 'Павел Новиков (aka VokiVon)'

"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
import cProfile

def test_erat(func):
    test_list = [2, 3, 5, 7, 11, 13, 17, 19]
    res = func(20)
    for i, item in enumerate(test_list):
        assert item == res[i]
        print(f"Test [{i}] = OK")



def erat_01(n):
    """
    Алгоритм "решето Эратосфера"
    :param n: число до которого нужно искать простые числа
    :return: массив простых чисел
    """

    sieve = [i for i in range(n)]

    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res

#  "Task_02.erat_01(100)"
# 100 loops, best of 3: 20.4 usec per loop
#  "Task_02.erat_01(200)"
# 100 loops, best of 3: 42.7 usec per loop
# "Task_02.erat_01(300)"
# 100 loops, best of 3: 69.2 usec per loop
# cProfile.run("erat_01(300)")
# 1    0.000    0.000    0.000    0.000 Task_02.py:21(erat_01) - 100
# 1    0.000    0.000    0.000    0.000 Task_02.py:21(erat_01) - 200
# 1    0.000    0.000    0.000    0.000 Task_02.py:21(erat_01) - 300


def erat_02(n):
    """
    Алгоритм - перебор делением с проверкой остатка
    :param n: число до которого нужно искать простые числа
    :return: массив простых чисел
    """

    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
            j = i + 1
            while j < n:
                if sieve[j] != 0 and sieve[j] % i == 0:
                    sieve[j] = 0
                j += 1

    res = [i for i in sieve if i != 0]
    return res
# "Task_02.erat_02(100)"
# 100 loops, best of 3: 443 usec per loop
# "Task_02.erat_02(200)"
# 100 loops, best of 3: 1.75 msec per loop
# "Task_02.erat_02(300)"
# 100 loops, best of 3: 4.19 msec per loop
# cProfile.run("erat_02(300)")
# 1    0.000    0.000    0.000    0.000 Task_02.py:53(erat_02) - 100
# 1    0.002    0.002    0.002    0.002 Task_02.py:53(erat_02) - 200
# 1    0.004    0.004    0.004    0.004 Task_02.py:53(erat_02) - 300



def erat_03(n):
    """
    Алгоритм - пока не придумал
    :param n: число до которого нужно искать простые числа
    :return: массив простых чисел
    """
    FIRST = 2
    arr_ = [FIRST]
    num = FIRST
    idx = 1
    while True:
        idx += 1
        num = idx + idx - 1
        if num > n:
            break
        arr_.append(num)

    res = arr_
    return res


#test_erat(erat_01)
#test_erat(erat_02)

"""
py -m timeit -n 100 -s "import Task_02" "Task_02.erat_02(100)"
"""