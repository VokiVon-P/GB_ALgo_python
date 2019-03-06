__author__ = 'Павел Новиков (aka VokiVon)'
import collections
"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, 
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. 
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

"""
Решение:
Функции суммы и произведения решил каждую своим способом, хотя можно было и через сложение сделать
Также порезвился с разными коллекциями  ))) 
"""

HEXARR = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def dec_to_hex_one(d_num):
    return list(HEXARR.keys())[d_num]


def hex_to_dec_all(hex_):
    """
    Переводит число из 16ричного числа в 10ричное
    :param hex_: массив из символов шестнадцетиричного числа
    :return: десятичный int
    """
    res = 0
    for item in hex_:
        res *= 16
        tmp_ = HEXARR[item]
        res += tmp_
    return res


def dec_to_hex_all(num_):
    """
    Переводит число из 10ричного в 16ричное
    :param num_: десятичный int
    :return: массив из символов шестнадцетиричного числа
    """
    res = collections.deque()
    tmp_next = num_
    while tmp_next > 0:
        tmp_h = tmp_next % 16
        tmp_next //= 16
        res.appendleft(dec_to_hex_one(tmp_h))
    return list(res)


def hex_to_str(hex_):
    return ''.join(hex_)


def str_to_hex(hex_str):
    """
    преобразует сроку в список 16x числа
    :param hex_str: исходная строка
    :return: список 16x числа
    """
    return list(hex_str.upper())


def dec_hex_plus_help(dec1, dec2, dec_mem=0):
    """
    Складывает цифры 16_ричного числа в 10_ричном представлении
    :param dec1: первая цифра
    :param dec2: вторая цифра
    :param dec_mem: цифра из памяти ( из предыдущих сложений )
    :return: кортеж ( результат сложения цифр, цифра в память для следующего регистра )
    """
    tmp_res = dec1 + dec2 + dec_mem
    res_mem = tmp_res // 16
    res_num = tmp_res % 16
    return res_num, res_mem


def hex_plus(h_1, h_2):
    """
    складывает 2 16х числа
    :param h_1: 16х число в виде списка
    :param h_2: 16х число в виде списка
    :return: список содержащий результат сложения двух 16_ричных числа
    """
    res = collections.deque()
    mem = 0
    # копируем списки из аргументов, т.к дальше используем pop()
    hex_1 = h_1.copy()
    hex_2 = h_2.copy()

    while len(hex_1) or len(hex_2):
        if len(hex_1):
            tmp_h1 = HEXARR[hex_1.pop()]
        else:
            tmp_h1 = 0

        if len(hex_2):
            tmp_h2 = HEXARR[hex_2.pop()]
        else:
            tmp_h2 = 0

        # print(f"[{tmp_h1} + {tmp_h2} + {mem}]")
        tmp_ = dec_hex_plus_help(tmp_h1, tmp_h2, mem)
        num_ = dec_to_hex_one(tmp_[0])
        mem = tmp_[1]
        res.appendleft(num_)
    if mem:
        res.appendleft(dec_to_hex_one(mem))
    return list(res)


def hex_mult(hex_1, hex_2):
    """
     Умножает два 16х числа
    :param hex_1: первое 16х число
    :param hex_2: второе 16х число
    :return: произведение 16х чисел в виде списка
    """
    num_1 = hex_to_dec_all(hex_1)
    num_2 = hex_to_dec_all(hex_2)
    num_mult = num_1 * num_2
    return dec_to_hex_all(num_mult)


hex_str1 = input("Введите первое HEX число: ")
hex_str2 = input("Введите второе HEX число: ")
# hex_str1 = "A2"
# hex_str2 = "C4F"
print()
print(f"Первое число: {hex_str1}")
print(f"Второе число: {hex_str2}")
print()

hex_01 = str_to_hex(hex_str1)
hex_02 = str_to_hex(hex_str2)
hex_sum = hex_plus(hex_01, hex_02)
hex_mult = hex_mult(hex_01, hex_02)

print(hex_01)
print(hex_02)
print()
print(hex_sum)
print(hex_mult)
print()
print(f"Сумма цифр 0x{hex_str1} и 0x{hex_str2} = 0x{hex_to_str(hex_sum)}")
print()
print(f"Произведение цифр 0x{hex_str1} и 0x{hex_str2} = 0x{hex_to_str(hex_mult)}")
