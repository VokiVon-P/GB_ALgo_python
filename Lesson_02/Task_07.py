__author__ = "Павел Новиков (aka VokiVon)"
"""
7. Напишите программу, доказывающую или проверяющую, 
что для множества натуральных чисел выполняется равенство: 
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
n = int(input("Введите натуральное число n ( целое больше 0): "))

i = 1
m = 0
while i <= n:
    m = m+i
    i += 1

pr = int(n*(n+1)/2)

if pr == m:
    print(f"1+2+...n = n*(n+1)/2 ( {m} = {pr} )")
else:
    print(f"1+2+...n != n*(n+1)/2 ( {m} != {pr} )")
