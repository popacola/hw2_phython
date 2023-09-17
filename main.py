# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# import random
#
# n = int(input("Введите количество монет на столе: "))
# top_side = random.randint(1,n)
# bottom_side = n - top_side
# print(f"Орел: {top_side}. Решка: {bottom_side}")
#
# if top_side == bottom_side:
#     print("Количество монет, которые необходимо перевернуть:", top_side)
# elif top_side < bottom_side:
#     print("Количество монет, которые необходимо перевернуть:", top_side)
# else:
#     print("Количество монет, которые необходимо перевернуть:", bottom_side)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# def find_numbers(S, P):
#     for X in range(1, 1001):
#         for Y in range(1, 1001):
#             if X + Y == S and X * Y == P:
#                 return (X, Y)
#     return (-1, -1)
#
# input_str = input("Введите сумму (S) и произведение (P) чисел, разделенные пробелом: ")
# S, P = map(int, input_str.split())
#
# X, Y = find_numbers(S, P)
#
# if X == -1:
#     print("Невозможно определить числа")
# else:
#     print(f"Числа: {X} и {Y}")

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число N: "))
power = 1

while power <= n:
    print(power)
    power *= 2