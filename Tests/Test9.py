"""
Деловая колбаса
Настало время для действительно серьёзных задач...
В детском саду 2 ребенка съедают 2 куска колбасы за 2 минуты. Сколько кусков колбасы за N минут съедят M детей?

Формат ввода
В первой строке записано натуральное число N ≥ 1
Во второй строке записано натуральное число M ≥ 1

Формат вывода
Одно натуральное число — количество кусков колбасы, съеденных детьми

Примечание
Гарантируется, что в результате вычислений будет получено натуральное число.
"""

N = int(input()) # Количество минут
M = int(input()) # Количество детей
b = N / 2 # Формула расчета количества времени на съедение колбасы
c = M * b 
print(int(c))