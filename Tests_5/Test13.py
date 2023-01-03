"""
Массовое возведение в степень
Часто возникают трудности, когда нужно выполнить множество однообразных операций. 
В таких случаях люди желают упростить себе работу. Напишите программу, которая возводит в заданную степень все числа, 
что передали пользователи.

Формат ввода
Вводится натуральное число N — количество чисел.
В каждой из последующих N строк записано по одному числу.
В последней строке записано натуральное число P — степень, в которую требуется возвести числа.

Формат вывода
Последовательность чисел, являющихся ответом.

Ввод:
3
2
3
4
3

Вывод:
8
27
64
"""

number = int(input())
list_temp = []
for i in range(1, number + 1):
    temp = int(input())
    list_temp.append(temp)
    if i >= number:
        degree = int(input())
        for num in list_temp:
            print(num ** degree)
