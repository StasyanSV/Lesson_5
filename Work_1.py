# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".\
#
# some_text = 'моя кошка мыла раму в магазине'
#
# some_text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, some_text.split()))
# print(some_text_list)


# Реализовать RLE алгоритм.реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах.
#
# with open('encoded_text.txt', 'r') as file:
#     encoded_text = file.read()
# def encoding(data):
#     encoding = ''
#     prev_char = ''
#     count = 1
#
#     for char in encoded_text:
#         if char != prev_char:
#             if prev_char:
#                 encoding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encoding += str(count) + prev_char
#     return encoding
#
# with open('decoded_text.txt', 'r') as file:
#     decoded_text = file.read()
# def decoding(data):
#     decoding = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decoding += char * int(count)
#             count = ''
#     return decoding
#
# print(encoding(encoded_text))
# print(decoding(decoded_text))


# Создайте программу для игры в "Крестики-нолики".
#
# print("*" * 3, " Игра Крестики-нолики для двух игроков ", "*" * 3)
#
# some_list = list(range(1, 10))
#
# def draw_board(some_list):
#     for i in range(3):
#         print(f'| {some_list[0 + i * 3]} | {some_list[1 + i * 3]} | {some_list[2 + i * 3]} |')
#         print('-' * 13)
#
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input(f'Куда поставим {player_token}? ')
#       try:
#          player_answer = int(player_answer)
#       except:
#          print(f'Некорректный ввод. Вы уверены, что ввели число? ')
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(some_list[player_answer-1]) not in "XO"):
#             some_list[player_answer-1] = player_token
#             valid = True
#          else:
#             print(f'Эта клетка уже занята! ')
#       else:
#         print(f'Некорректный ввод. Введите число от 1 до 9. ')
#
# def check_win(board):
#    win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input(f'X')
#         else:
#            take_input(f'O')
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(f'{tmp} выиграл! ')
#               win = True
#               break
#         if counter == 9:
#             print(f'Ничья! ')
#             break
#     # draw_board(board)
# main(some_list)
#
# input(f'Нажмите Enter для выхода! ')
