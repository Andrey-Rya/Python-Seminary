# Это функция генерирует список случайных целых чисел

import random

def list_generation():
    n = int(input('Введите количество элементов вашего списка: '))
    b1 = int(input('Нижняя граница диапазона значений списка: '))
    b2 = int(input('Верхняя граница диапазона значений списка: '))
    return [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]
