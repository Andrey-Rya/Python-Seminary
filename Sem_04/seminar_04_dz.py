# 1. Вычислить число c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)
# from math import pi
#
# d = int(input("Округление числа Пи с точностью до этого количества знаков:\n"))
# print(f'число Пи с точностью до {d} знаков равно: {round(pi, d)}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример:
# N = 20 => [2, 2, 5]
#
# n = int(input("Введите натуральное число N: "))
# i = 2  # вводим первый простой множитель
# list = []
# number = n
# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Список простых множителей числа {number} составляет: {list}")
#

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Пример:
# [1, 2, 2, 3, 4] -> [1, 3, 4]

# lst = list(map(int, input("Введите последовательность чисел через пробел:\n").split()))
# print(f"Ваша последовательность чисел: {lst}")
# unique = [i for i in lst if lst.count(i) == 1]
# print(f'Список неповторяющихся элементов в вашей последовательности: {unique}')

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools
#
# k = randint(2, 7)
#
# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios
#
# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
#
#
# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)
#
# with open('file.txt', 'w') as data:
#     data.write(polynom1)

# Это многочлен для следующей задачи:

# k = randint(2, 5)
#
# ratios = get_ratios(k)
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)
#
# with open('file_2.txt', 'w') as data:
#     data.write(polynom2)

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример
# poly_1: 2x^2 + 5x + 7
# poly_2: 5x^2 + 7x + 1
# результат: 7x^2 + 12x + 8

# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x + 7')
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('5*x^2 + 7*x + 1')
#
# with open('poly_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()
#
#
# with open('poly_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()
#
# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = '7x^2 + 12x + 8'
# print(f'Сумма многочленов равняется {sum_poly}')
#
# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{sum_poly}')
#

