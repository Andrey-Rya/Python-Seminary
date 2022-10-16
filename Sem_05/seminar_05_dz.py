# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Данные на входе: 'привет забвение пока'
# Данные на выходе: 'привет пока'
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Данные на входе: 'привет забвение пока'
# Данные на выходе: 'привет пока'

# txt = input("Введите пожалуйста текст через пробел:\n")
# print(f"Вы ввели текст: {txt}")
# find_txt = "абв"
# list = [i for i in txt.split() if find_txt not in i]
# print(f'Ваш результат без слов, содержащих символы абв: {" ".join(list)}')

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, Введите количество конфет, которое Вы возьмете (от 1 до 28): "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, Некорректный ввод. Повторите команду!: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ход сделал {name}, и он взял {k} конфет(ы), теперь у него {counter} конфет. На столе осталось {value} конфет(ы).")
#
# def bot_calc(value):
#     k = randint(1,29)
#     while value-k <= 28 and value > 29:
#         k = randint(1,29)
#     return k
#
# player1 = input("Имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # это флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# 3. Создайте программу для игры в "Крестики-нолики".

# coding: utf8
X = "X"
O = "O"
EMPTY = ' '
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    '''инструкция для игроков'''
    print(
 """
  Это игра Крестики-нолики! Вы играете против компьютера.
 Для того, что бы сделать свой ход, введите цифру от 0 до 8.
 Числа соответсвуют полям доски ниже:
 0 | 1 | 2
 ---------
 3 | 4 | 5
 ---------
 6 | 7 | 8
 Приготовьтесь к игре! Сейчас начнется решающее сражение!\n
 """
         )
def ask_yes_no(question):
     """Задает вопросы с ответом 'Да' или 'Нет".    """
     response = None
     while response not in ("y", "n"):
         response = input(question).lower()
     return response
def ask_number(question, low, high):
     """Ввод числа из диапазона."""
     response = None
     while response not in range(low,high):
         response = int(input(question))
     return response

def pieces():
     "Выбор первого хода"
     go_first = ask_yes_no("Желаете оставить за собой первый ход?(y/n): ")
     if go_first == "y":
         print("\n Ну что ж ,даю тебе фору играй крестиками")
         human = X
         computer = O
     else:
         print("\n Спасибо за то, что Вы предоставили право первого хода компьютеру")
         computer = X
         human = O
     return computer, human
def new_board():
     "Создает новую игровую доску"
     board = []
     for square in range(NUM_SQUARES):
         board.append(EMPTY)
     return board
def  display_board(board):
     """Отображает  игровую  доску  на  экране."""
     print("\n\t", board[0], "|", board[1], "|", board[2])
     print("\t",  "---------")
     print("\n\t", board[3], "|", board[4],  "|", board[5])
     print("\t",  "---------")
     print("\n\t", board[6], "|", board[7],  "|",  board[8], "\n")

def legal_moves(board):
     """Создает список доступных ходов """
     moves=[]
     for square in range(NUM_SQUARES):
         if board[square] == EMPTY:
             moves.append(square)
     return moves
def winner(board):
     """Определяет победителя в игре """
     ways_to_win=((0, 1, 2),
                  (3, 4, 5),
                  (6, 7, 8),
                  (0, 3, 6),
                  (1, 4, 7),
                  (2, 5, 8),
                  (0, 4, 8),
                  (2, 4, 6))
     for row in ways_to_win:
         if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
             winner = board[row[0]]
             return winner
         if EMPTY not in board:
             return TIE
     return None

def human_move(board,human):
     """ Получает ход человека"""
     legal = legal_moves(board)
     move = None
     while move not in legal:
         move = ask_number("Ваш ход. Выберите одно из полей (0-8):", 0, NUM_SQUARES)
         if move not in legal:
             print("\nВы невнимательный человек! Это поле уже занято. Выберите другое.\n")
     print("Хорошо.....")
     return move
def computer_move(board, computer, human):
     """Ход делает компьютер """
     #создание рабочей копии доски, потому что функция будет менять некоторые значения в списке
     board = board[:]
     #поля от лучшего к худшему
     BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
     print("Я выберу номер", end=" ")
     for move in legal_moves(board):
         board[move] = computer
         #Если следующим ходом может победить компьютер,выбераем ход
         if winner(board) == computer:
             print(move)
             return move
         #выполним проверку, отменим внесения изменения
         board[move]=EMPTY
     #  поскольку следующим ходом  ни  одна  сторона  не  может  победить.
     #  выберем лучшее из  доступных  полей
     for move in BEST_MOVES:
         if move in legal_moves(board):
             print(move)
             return move
def next_turn(turn):
     """Делает переход хода."""
     if turn == X:
         return O
     else:
         return X
def congrat_winner(the_winner, computer, human):
     """Поздравляем;  победителя  игры."""
     if the_winner != TIE:
         print("Три", the_winner, "в ряд!\n")
     else:
         print("Ничья!\n")
     if the_winner == computer:
         print("Победил компьютер!")
     elif the_winner==human:
         print("Поздравляю,Вы победили компьютер!")
     elif the_winner==TIE:
         print("Ничья!")
def main():
     """Основная часть программы """
     display_instruct()
     computer, human = pieces()
     turn = X
     board = new_board()
     display_board(board)
     while not winner(board):
         if turn == human:
             move=human_move(board, human)
             board[move] = human
         else:
             move=computer_move(board, computer, human)
             board[move]=computer
         display_board(board)
         turn = next_turn(turn)
     the_winner=winner(board)
     congrat_winner(the_winner, computer, human)

 #Старт программы
main()
input("\n\nНажмите любую кнопку для выхода.")

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W
#
# with open('file_encode.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
#
# with open('file_encode.txt', 'r') as data:
#     string = data.readline()
#
# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string
#
#
# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)
#
#     return decoded_string
#
#
# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()
#
# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)
#
# print('Декодированная строка: \t' + decoded_string)
# print('Закодированная строка: \t' + rle_encode(decoded_string))
# print(f'Степень сжатия: \t{round(len(decoded_string) / len(encoded_string), 1)}')

# txt = input("Введите пожалуйста текст через пробел:\n")
# print(f"Вы ввели текст: {txt}")
# find_txt = "абв"
# list = [i for i in txt.split() if find_txt not in i]
# print(f'Ваш результат без слов, содержащих символы абв: {" ".join(list)}')

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, Введите количество конфет, которое Вы возьмете (от 1 до 28): "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, Некорректный ввод. Повторите команду!: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ход сделал {name}, и он взял {k} конфет(ы), теперь у него {counter} конфет. На столе осталось {value} конфет(ы).")
#
# def bot_calc(value):
#     k = randint(1,29)
#     while value-k <= 28 and value > 29:
#         k = randint(1,29)
#     return k
#
# player1 = input("Имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # это флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# 3. Создайте программу для игры в "Крестики-нолики".
#coding: utf8
# X = "X"
# O = "O"
# EMPTY = ' '
# TIE = "Ничья"
# NUM_SQUARES=9
#
# def display_instruct():
#     '''инструкция для игроков'''
#     print(
# """
#  Это игра Крестики-нолики! Вы играете против компьютера.
# Для того, что бы сделать свой ход, введите цифру от 0 до 8.
# Числа соответсвуют полям доски ниже:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8
# Приготовься к игре! Сейчас начнется решающее сражение!\n
# """
#         )
# def ask_yes_no(question):
#     """Задает вопросы с ответом 'Да' или 'Нет".    """
#     response = None
#     while response not in ("y", "n"):
#         response = input(question).lower()
#     return response
# def ask_number(question, low, high):
#     """Ввод числа из диапазона."""
#     response = None
#     while response not in range(low,high):
#         response = int(input(question))
#     return response
# def pieces():
#     "Выбор первого хода"
#     go_first = ask_yes_no("Хочешь оставить за собой первый ход?(y/n): ")
#     if go_first == "y":
#         print("\n Ну что ж ,даю тебе фору играй крестиками")
#         human = X
#         computer = O
#     else:
#         print("\n Спасибо за то, что дал право первого хода компьютеру")
#         computer = X
#         human = O
#     return computer, human
# def new_board():
#     "Создает новую игровую доску"
#     board = []
#     for square in range(NUM_SQUARES):
#         board.append(EMPTY)
#     return board
# def  display_board(board):
#     """Отображает  игровую  доску  на  экране."""
#     print("\n\t", board[0], "|", board[1],"|",board[2])
#     print("\t",  "---------")
#     print("\n\t", board[3], "|", board[4],  "|", board[5])
#     print("\t",  "---------")
#     print("\n\t", board[6], "|", board[7],  "|",  board[8], "\n")
#
# def legal_moves(board):
#     """Создает список доступных ходов """
#     moves=[]
#     for square in range(NUM_SQUARES):
#         if board[square] == EMPTY:
#             moves.append(square)
#     return moves
# def winner(board):
#     """Определяет победителя в игре """
#     WAYS_TO_WIN=((0, 1, 2),
#                  (3, 4, 5),
#                  (6, 7, 8),
#                  (0, 3, 6),
#                  (1, 4, 7),
#                  (2, 5, 8),
#                  (0, 4, 8),
#                  (2, 4, 6))
#     for row in WAYS_TO_WIN:
#         if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
#             winner = board[row[0]]
#             return winner
#         if EMPTY not in board:
#             return TIE
#     return None
#
# def human_move(board,human):
#     """ Получает ход человека"""
#     legal = legal_moves(board)
#     move = None
#     while move not in legal:
#         move = ask_number("Твой ход. Выбери одно из полей (0-8):", 0, NUM_SQUARES)
#         if move not in legal:
#             print("\nВы невнимательный человек! Это поле уже занято. Выбери другое.\n")
#     print("Хорошо.....")
#     return move
# def computer_move(board, computer, human):
#     """Ход делает компьютер """
#     #создание рабочей копии доски, потому что функция будет менять некоторые значения в списке
#     board = board[:]
#     #поля от лучшего к худшему
#     BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
#     print("Я выберу номер", end=" ")
#     for move in legal_moves(board):
#         board[move] = computer
#         #Если следующим ходом может победить компьютер,выбераем ход
#         if winner(board) == computer:
#             print(move)
#             return move
#         #выполним проверку, отменим внесения изменения
#         board[move]=EMPTY
#     #  поскольку следующим ходом  ни  одна  сторона  не  может  победить.
#     #  выберем лучшее из  доступных  полей
#     for move in BEST_MOVES:
#         if move in legal_moves(board):
#             print(move)
#             return move
# def next_turn(turn):
#     """Делает переход хода."""
#     if turn == X:
#         return O
#     else:
#         return X
# def congrat_winner(the_winner, computer, human):
#     """Поздравляем;  победителя  игры."""
#     if the_winner != TIE:
#         print("Три", the_winner, "в ряд!\n")
#     else:
#         print("Ничья!\n")
#     if the_winner == computer:
#         print("Победил компьютер!")
#     elif the_winner==human:
#         print("Поздравляю,Вы победили компьютер!")
#     elif the_winner==TIE:
#         print("Ничья!")
# def main():
#     """Основная часть программы """
#     display_instruct()
#     computer, human = pieces()
#     turn = X
#     board = new_board()
#     display_board(board)
#     while not winner(board):
#         if turn == human:
#             move=human_move(board, human)
#             board[move] = human
#         else:
#             move=computer_move(board, computer, human)
#             board[move]=computer
#         display_board(board)
#         turn = next_turn(turn)
#     the_winner=winner(board)
#     congrat_winner(the_winner, computer, human)
#
# #Старт программы
#
# main()
# input("\n\nНажмите любую кнопку для выхода.")

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W
#
# with open('file_encode.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
#
# with open('file_encode.txt', 'r') as data:
#     string = data.readline()
#
# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string
#
#
# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)
#
#     return decoded_string
#
#
# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()
#
# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)
#
# print('Декодированная строка: \t' + decoded_string)
# print('Закодированная строка: \t' + rle_encode(decoded_string))
# print(f'Степень сжатия: \t{round(len(decoded_string) / len(encoded_string), 1)}')
