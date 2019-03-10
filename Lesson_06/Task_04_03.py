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
arr_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(arr_)


# Решаем через count() и нахождение максимума
freq_max = 1  # если максимум равен 1 значит элементы не повторяются
item_max = None

for item in arr_:
    temp = arr_.count(item)
    if temp > freq_max:
        freq_max = temp
        item_max = item

if item_max is not None:
    print(f'Число {item_max} встречается наибольшее количество ({freq_max}) раз!')
else:
    print('Элементы не повторяются')

