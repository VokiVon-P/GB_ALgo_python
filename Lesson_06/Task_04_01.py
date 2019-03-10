from sys import version
import platform

__author__ = 'Павел Новиков (aka VokiVon)'
"""
Определить, какое число в массиве встречается чаще всего.
"""

import Lesson_06.generator as gen
# from Lesson_06.generator import doble_check

# переопределяем переменные генератора для получения дублей в массиве
gen.min_item = 0
gen.max_item = 9
gen.size = 20

# arr_ = gen.gen_array()
arr_ = [1, 1, 9, 8, 4, 5, 7, 2, 7, 5, 0, 6, 5, 0, 1, 4, 1, 9, 6, 1]
print(arr_)

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

if out_item is not None:
    print(f'Число {out_item} встречается наибольшее количество ({freq}) раз!')
else:
    print('Элементы не повторяются')

# ======================================================
# блок служебной информации по расчету занимаемой памяти
print()
print('='*60)
print("Блок служебной информации по расчету занимаемой памяти")
print('='*60)

mem_size = 0
mem_size += gen.doble_check(arr_)
mem_size += gen.doble_check(freq)
mem_size += gen.doble_check(out_item)
mem_size += gen.doble_check(dict_freq)

print(f"Python version: {version}")
print(f"Архитектура системы: {platform.architecture()}")

print('='*60)
print(f"Размер вычисленный через глобальную переменную: {gen.mem_size_counter}")
print(f"Размер полученный с помощью локальных вычислений: {mem_size}")
print('='*60)
