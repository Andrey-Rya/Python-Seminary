# -*- coding: utf-8 -*-

# === 1 задача (1 вариант) ===
# Даны три целых числа. Определите, сколько среди них
# совпадающих. Программа должна вывести одно из чисел: 3
# (если все совпадают), 2 (если два совпадает) или 0
# (если все числа различны).

# a = int(input('Введите первое число: '))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if a == b == c:
#     print('Все 3 введенных числа совпадают')
# elif a == b or b == c or c == a:
#     print('Совпали 2 введенных числа')
# else:
#     print('Совпадений нет!')

# === 1 задача (2 вариант) ===
# a = int(input('Введите первое число: '))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# def GetNum(a, b, c):
#     if a == b == c:
#         return 3
#     if a == b or b == c or a == c:
#         return 2
#         return 0
# print(GetNum(a, b, c))


# === 2 задача (1 вариант) ===
# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B
# включительно, в порядке убывания. В этой задаче можно обойтись без
# инструкции if
# a = int(input('Введите число А: '))
# b = int(input("Введите число B: "))
# a = a - (a+1) % 2  # делаем a - нечетным числом
# for i in range(a, b-2, -2):
#     print(i)

# === 2 задача (2 вариант) ===
# a = int(input('Введите число A: '))
# b = int(input("Введите число B: "))
# b = b+(b + 1) % 2  # делаем b - нечетным числом
# k = []
# for i in range(b, a+1, 2):
#     k.append(i)
#     k = k[:: -1]
# print(*k)

# === 3 задача ===
# Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.
# пример: Для N = 5: 1, -3, 9, -27, 81
# n = int(input('Введите число N: '))
# for i in range(n):  # range(0, 5, 1)
#     result = (-3)**i
#     print(result, end=", ")


# # === 4 задача ===
# Напишите программу, которая проверяет пятизначное число на палиндром.
# paltus = input('Введите число: ')
# if paltus[:2] == paltus[:2:-1]:
#     print('палиндром')
# else:
#     print('Не палиндром')


# Удалить вторую цифру трёхзначного числа.
# a = 486
# print(a // 100 * 10 + a % 10)

# === 6 задача ===
#	Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.
# s = input('Введите строку s: ')
# s1 = input('Введите строку s1: ')
# print(s.count(s1))
