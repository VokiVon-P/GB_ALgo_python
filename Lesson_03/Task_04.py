__author__ = 'Павел Новиков (aka VokiVon)'
"""
Определить, какое число в массиве встречается чаще всего.
"""

import Lesson_03.generator as gen

# переопределяем переменные генератора для получения дублей в массиве
gen.min_item = 0
gen.max_item = 5
gen.size = 20

arr_ = gen.gen_array()
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
