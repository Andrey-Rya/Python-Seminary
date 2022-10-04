# 1. Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


# def Chislo(number):
#     YES = False
#     while not YES:
#         try:
#             num = float(input(f"{number}"))
#             YES = True
#         except ValueError:
#             print("Ошибка при вводе. Введите число!")
#     return num


# def summa(n):  # подсчет суммы чисел
#     s = 0
#     for i in str(n):
#         if i != ".":
#             s += int(i)
#     return s


# n = Chislo("Введите вещественное число: ")
# print(f"Сумма всех цифр = {summa(n)}")

# 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда[1, 2, 6, 24](1, 12, 123, 1234)

# n = int(input("Введите число N:  "))
# fact = 1
# print('[', end='')
# for i in range(1, n+1):
#     fact *= i
#     print(f'', fact, end=',')
# print(']', end='')

# 3. Задайте список из n чисел последовательности (1+1/n)^n выведите
#  на экран их сумму.
# n = int(input("Введите число N:  "))
# # считаем последовательность и округл до 2 знаков
# list = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# # вывод чисел и суммы с округлением до 2-х знаков
# print(f'последовательность чисел: {list}\nсумма чисел: {round(sum(list), 2)}')

# 4. Задайте список из N элементов, заполненных числами из промежутка
#  [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3]. Найдите произведение
# элементов на указанных позициях.

# N = int(input('Количество N элементов = '))
# numbers = []
# for i in range(-N, N+1):
#     numbers.append(i)
#     # numbers.append(randint(-N, N+1)) # можно заполнить список случайными числами

# print(f'Список элементов от -{N} до {N}: {numbers}')


# def get_num(numbers):
#     count = 0
#     for element in numbers:
#         count += 1
#     return count


# print('Общее количество элементов: ', get_num(numbers))

# print(f'Введите индекс первого элемента от 0 до {get_num(numbers)-1}')
# x = int(input())
# print(f'Введите индекс второго элемента от 0 до {get_num(numbers)-1}')
# y = int(input())

# for i in range(len(numbers)):
#     mult = numbers[x]*numbers[y]

# print(f'Умножение указанных элементов: {numbers[x]} * {numbers[y]} =', mult)


# 5. Реализуйте алгоритм перемешивания списка (метод random.shuffle
# использовать нельзя, но другие методы из библиотеки random - можно).

# from random import Random, randint
# N = int(input('Введите количество элементов списка: '))
# num = []
# for i in range(N):
#     num.append(randint(-N, N+1))
# print(f'Ваш список случайных чисел: {num}')


# def mix(number):
#     list = number[:]
#     numbers_length = len(list)
#     for i in range(numbers_length):
#         index = randint(0, numbers_length - 1)
#         temporary = list[i]
#         list[i] = list[index]
#         list[index] = temporary
#     return list


# print(f'Список после перемешивания: {mix(num)}')
