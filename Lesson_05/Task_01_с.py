import collections
import random

__author__ = 'Павел Новиков (aka VokiVon)'
"""
1. Пользователь вводит данные о количестве предприятий, 
их наименования и прибыль за 4 квартала 
(т.е. 4 отдельных числа) для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) 
и вывести наименования предприятий, чья прибыль выше среднего 
и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

# Решение с использованием collections

Report = collections.namedtuple('Report', ['title', 'q_4', 'year_sum'])

reports = collections.deque()
avg_r = 0
sum_all = 0

count_r = int(input(f"Введите количество предприятий: "))
# проверка на положительное кол-во
if count_r <= 0:
    print(f"Введено некорректное значение кол-ва предриятий {count_r}")
    exit(0)

# блок ввода данных
for i in range(count_r):
    r_name = input("\nВведите название предприятия: ")
    # ввод квартальных прибылей
    data_q = list()
    for j in range(4):
        data_q.append(int(input(f"Введите прибыль {j+1} квартала: ")))
        # data_q.append(random.randint(10, 99))
    sum_y = sum(data_q)
    sum_all += sum_y
    rep = Report(r_name, data_q, sum_y)
    reports.append(rep)

avg_r = sum_all / count_r
print("\nВведенные данные:")
print(*reports, sep='\n')
print("\n")
print(f"Общая прибыль за год всех предприятий: {sum_all}")
print(f"Средняя годовая прибыль: {avg_r}")

# проходим за один раз и используем разное добавление элементов в список
up_list = []
low_list = []
for item in reports:
    if item.year_sum > avg_r:
        up_list.append(item.title)
    elif item.year_sum < avg_r:
        low_list += [item.title]

# up_list = [item.title for item in reports if item.year_sum > avg_r]
# low_list = [item.title for item in reports if item.year_sum < avg_r]

# вывод результатов
print("Предприятия с прибылью выше средней: ", end="")
print(*up_list, sep='\t\t')
print("Предприятия с прибылью ниже средней: ", end="")
print(*low_list, sep='\t\t')




