__author__ = 'Павел Новиков (aka VokiVon)'
"""
В диапазоне натуральных чисел от 2 до 99 определить, 
сколько из них кратны любому из чисел в диапазоне от 2 до 9
"""

START_RANGE = 2
END_RANGE = 99

FIRST_DIGIT = 2
LAST_DIGIT = 9


def check_digit(range_, digit_check):
    """
    считает кол-во кратных чисел в диапазоне
    + доп проверка входных параметров: (0 и 1) исключаются
    :return: кол-во кратных чисел
    """
    if digit_check in {0, 1}:
        return 0

    out_count = 0
    for j in range_:
        if not j % digit_check:
            out_count += 1
    return out_count


range_test = range(START_RANGE, END_RANGE+1)
for i in range(FIRST_DIGIT, LAST_DIGIT+1):
    print(f"Числу {i} кратно {check_digit(range_test, i)} чисел'")
