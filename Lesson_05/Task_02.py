__author__ = 'Павел Новиков (aka VokiVon)'
import collections
"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, 
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. 
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

HEXARR = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def dec_to_hex_one(d_num):
    return list(HEXARR.keys())[d_num]

def hex_to_dec_all(hex_):
    res = 0;
    for item in hex_:
        res *= 16
        tmp_ = HEXARR[item]
        res += tmp_
    return res



def dec_plus_help(dec1, dec2, dec_mem = 0):
    tmp_res = dec1 + dec2 + dec_mem
    res_mem = tmp_res // 16
    res_num = tmp_res % 16
    return res_num, res_mem


def hex_plus(hex_1, hex_2):
    res = collections.deque()
    mem = 0
    while len(hex_01) or len(hex_02):
        if len(hex_01):
            tmp_h1 = HEXARR[hex_01.pop()]
        else:
            tmp_h1 = 0

        if len(hex_02):
            tmp_h2 = HEXARR[hex_02.pop()]
        else:
            tmp_h2 = 0

        print(f"[{tmp_h1} + {tmp_h2} + {mem}]")

        tmp_ = dec_plus_help(tmp_h1, tmp_h2, mem)
        num_ = dec_to_hex_one(tmp_[0])
        mem = tmp_[1]
        res.appendleft(num_)
    if mem:
        res.appendleft(dec_to_hex_one(mem))
    return list(res)

def hex_mult(hex_1, hex_2):
    return 0


#hex_str1 = input("Введите первое HEX число: ")
#hex_str2 = input("Введите второе HEX число: ")
hex_str1 = "1F"
hex_str2 = "FFF"
print(hex_str1)
print(hex_str2)

hex_01 = [i for i in hex_str1]
hex_02 = [i for i in hex_str2]
print(hex_01)
print(hex_02)
print()

hex_sum = hex_plus(hex_01, hex_02)
print(hex_sum)
str_1 = ""
print(f"Сумма цифр 0x{hex_str1} и 0x{hex_str2} = 0x{''.join(hex_sum)}")

print(hex_to_dec_all([i for i in hex_str1]))



#hex_02 = collections.deque()

