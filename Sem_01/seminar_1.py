# -*- coding: utf-8 -*-

# === 1 задача ===
# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число 
# квадратом другого

# a = int(input('Введите первое число: ')) # вводим число на ввод
# b = int(input("Введите второе число: ")) # вводим число на ввод
# if a ** 2 == b:
#     print('Да')
# elif b ** 2 == a:
#     print('Да')
# else:
#     print('Нет') 

# === 2 задача (1 вариант) ===
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
# m = int(input('Введите по-очереди 5 чисел:\n '))
# for i in range(4):
#     x = int(input())
#     if x > m:
#         m = x
# print(f'Максимальное число = {m}')

# # === 2 задача (2 вариант) ===
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
# sp = list() # заводим пустой список или sp = []
# for i in range(5):
#     x = int(input())
#     sp.append(x) # добавить список
# print(max(sp)) # ф-ция мах выведет максимальное число как min и sum

# # === 2 задача (3 вариант) только для положительных чисел ===
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
# m = 0
# for i in range(5): # range(0, 5, 1)
#     x = int(input())
#     if x > m:
#         m = x
# print(m)

# # === 3 задача (1 вариант)===
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# n = int(input('Введите начальное число: '))
# for i in range(-n, n + 1):
#     print(i, end=' ') # end='' -параметр именованной функции

# # === 3 задача (2 вариант)===
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# n = int(input('Введите начальное число: '))
# a = ''
# for i in range(-n, n + 1):
#     a = a + str(i)
#     a = a + ', '
# print(a)

# # 4 задача (1 вариант)
# # Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# n = float(input('Введите число с запятой: '))
# if n == int(n): # проверка на наличие дробной части
#     print('нет')
# else:
#     print(int(n * 10) % 10)

# # 4 задача (2 вариант)
# # Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# n = float(input('Введите число с запятой: '))
# n = (int(n * 10)) % 10 
# if n == 0: # if n == int(n)
#     print('нет')
# else:
#     print(round(n))

# 5 задача (1 вариант)
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# n = int(input("Введите число: "))
# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print('кратно')
# else:
#     print('нет')

# 5 задача (2 вариант)
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# n = int(input("Введите число: "))
# if n % 30 == 0:
#     print("Не подходит!")
# elif (n % 5 == 0 and n % 10 == 0 or n % 15 == 0):
#     print('Отлично! Подходит')
# else:
#     print('Нет')
