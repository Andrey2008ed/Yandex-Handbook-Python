"""
Простая задача 5.0

Напишите функцию is_prime, которая принимает натуральное число, а возвращает булево значение: 
True — если переданное число простое, а иначе — False.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
result = is_prime(1001459)

Вывод:
result = True
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
