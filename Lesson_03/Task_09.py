__author__ = 'Павел Новиков (aka VokiVon)'
"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import Lesson_03.generator as gen

# переопределяем переменные генератора для получения натуральных чисел
gen.min_item = 0
gen.size = 3

matrix = gen.gen_matrix()
print(*matrix, sep='\n')

out_max = None

SIZE_X = len(matrix[0])
SIZE_Y = len(matrix)

for i in range(SIZE_X):
    # мин = первый элемент колонки
    min_col = matrix[0][i]

    for j in range(SIZE_Y):
        # проходимся по колонке (поменяв индексы колонки и строки местами)
        temp = matrix[j][i]
        if temp < min_col:
            min_col = temp

    # сверка с предыдущим значением
    if out_max is None or out_max < min_col:
        out_max = min_col

print(f'Максимальный элемент из минимальных значений столбцов = {out_max}')
