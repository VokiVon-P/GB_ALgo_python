__author__ = 'Павел Новиков (aka VokiVon)'

"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections


TEXT = "мама мыла раму"
L_STEP = '0'
R_STEP = '1'


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def ins_in_list(lst_, node_, node_num_):
    """
    Добавляем в нужное место списка узел дерева
    :param lst_: список со значениями
    :param node_: узел
    :param node_num_: сумма чисел для узла
    """
    idx = None
    for item in lst_:
        if item[1] >= node_num_:
            idx = lst_.index(item)
            break

    if idx is None:
        lst_.append((node_, node_num_))
    else:
        lst_.insert(idx, (node_, node_num_))


def tree_search(bin_tree, steps=''):
    """
    Добавляем в словарь созданные последовательности шагов
    :param bin_tree: дерево обхода
    :param steps: шаги
    """
    if bin_tree.value is not None:
        dict_hoff[bin_tree.value] = steps
    if bin_tree.left is not None:
        tree_search(bin_tree.left, steps=f'{steps}{L_STEP}')
    if bin_tree.right is not None:
        tree_search(bin_tree.right, steps=f'{steps}{R_STEP}')


# разбираем строку по частоте и создаем отсортированный массив кортежей буква - частота
print(TEXT)
arr = collections.Counter(TEXT).most_common()
print(arr)
node_list = collections.deque(i for i in arr[::-1])
print(node_list)

# собираем дерево
while len(node_list) > 1:
    left_N = node_list.popleft()
    right_N = node_list.popleft()
    node_num = left_N[1] + right_N[1]

    if type(left_N[0]) is MyNode:
        node_left = left_N[0]
    else:
        node_left = MyNode(left_N[0])

    if type(right_N[0]) is MyNode:
        node_right = right_N[0]
    else:
        node_right = MyNode(right_N[0])

    node = MyNode(None, node_left, node_right)
    ins_in_list(node_list, node, node_num)
    # print(node_list)

# Пробегаем по дереву и заполняем словарь
dict_hoff = dict()
tree_search(node_list[0][0])

# печать словаря
print('\n Словарь для метода Хаффмана')
for i in dict_hoff.keys():
    print(f'\t\'{i}\'\t\t{dict_hoff[i]}')

# кодируем строку
print('\nКодируем строку:')
print(f'\n {TEXT}')
str_out = ''
for i in TEXT:
    str_out = f'{str_out} {dict_hoff[i]}'

print(f'{str_out}')
