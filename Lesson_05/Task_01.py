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

reports = {}
sum_r = 0
avg_r = 0

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
        #data_q.append(random.randint(10, 100))

    sum_r += sum(data_q)
    reports[r_name] = data_q

avg_r = sum_r/count_r
print("\nВведенные данные:")
print(reports)
print(f"Общая прибыль за год всех предприятий: {sum_r}")
print(f"Средняя годовая прибыль: {avg_r}")
# генерируем списки выше и ниже средней (можно и в один цикл с двумя условиями сделать)
up_list = [item for item in reports.keys() if sum(reports[item]) > avg_r]
low_list = [item for item in reports.keys() if sum(reports[item]) < avg_r]
# вывод результатов
print("Предприятия с прибылью выше средней: ", end="")
print(*up_list, sep='\t\t')
print("Предприятия с прибылью ниже средней: ", end="")
print(*low_list, sep='\t\t')




