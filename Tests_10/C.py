"""
Длина числа
Разработайте функцию number_length, которая принимает одно целое число и возвращает его длину без учёта знака.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
result = number_length(12345)

Вывод:
result = 5
"""

def number_length(num):
    num = num * -1 if num < 0 else num
    return len(str(num))