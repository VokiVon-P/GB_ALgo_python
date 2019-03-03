__author__ = 'Павел Новиков (aka VokiVon)'
"""
7. В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import Lesson_03.generator as gen

# переопределяем переменные генератора для получения натуральных чисел
gen.min_item = 0

arr_ = gen.gen_array()
print(arr_)

min_01 = arr_[0]
min_02 = arr_[1]

for item in arr_:
    if item < min_01:
        min_02 = min_01
        min_01 = item
    elif item < min_02:
        min_02 = item

print(f'Самое минимальное число {min_01} в ячейке {arr_.index(min_01)}')
print(f'Второе минимальное число {min_02} в ячейке {arr_.index(min_02)}')
