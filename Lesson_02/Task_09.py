__author__ = "Павел Новиков (aka VokiVon)"
"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.
"""

def Sum_Digit( num ):
    #################
    # Возвращает сумму входящих цифр числа аргумента

    a = num
    sum = 0;
    while a > 0:
        b = a % 10
        sum += b
        a = a // 10
    return sum

outSum = 0
outNum = 0
while True:
    n = int(input("Введитите натуральное число n ( целое больше 0) 0 - конец ввода: "))
    if n == 0:
        break

    s = Sum_Digit(n)
    if outSum < s:
        outSum = s
        outNum = n

print(f"Максимальная сумма цифр = {outSum} у числа {outNum}")


