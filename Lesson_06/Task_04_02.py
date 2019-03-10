__author__ = 'Павел Новиков (aka VokiVon)'
"""
Определить, какое число в массиве встречается чаще всего.
"""

import Lesson_06.generator as gen
import collections


# переопределяем переменные генератора для получения дублей в массиве
gen.min_item = 0
gen.max_item = 9
gen.size = 20

# arr_ = gen.gen_array()
arr_ = [1, 1, 9, 8, 4, 5, 7, 2, 7, 5, 0, 6, 5, 0, 1, 4, 1, 9, 6, 1]
#arr_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(arr_)


# создадим словарь где ключ - значение элемента массива,
# а значение элемента словаря - частота встречи
freq_counter = collections.Counter(arr_)
out_item = freq_counter.most_common(1)[0]

if out_item[1] > 1:
    print(f'Число {out_item[0]} встречается наибольшее количество ({out_item[1]}) раз!')
else:
    print('Элементы не повторяются')

# ======================================================
# блок служебной информации по расчету занимаемой памяти
# В конце дополнительно выведем инфу по всем сложным элементам и коллекциям
print()
print('='*60)
print("Блок служебной информации по расчету занимаемой памяти")
print('='*60)

mem_size = 0
mem_size += gen.doble_check(arr_)
mem_size += gen.doble_check(out_item)
mem_size += gen.doble_check(freq_counter)

print('='*60)
print(f"Размер вычисленный через глобальную переменную: {gen.mem_size_counter}")
print(f"Размер полученный с помощью локальных вычислений: {mem_size}")
print('='*60)

# Подробный расчет сложным элементов - можно закомментировать
print("Рассчет первоначального массива")
gen.ext_show_size(arr_, True)
print()
print("Рассчет Counter от массива")
gen.ext_show_size(freq_counter, True)
print()
print("Рассчет элемента Counter")
gen.ext_show_size(out_item, True)

