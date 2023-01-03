'''
Рассмотрим некоторые полезные функции библиотеки itertools.

Функции библиотеки itertools можно разделить на следующие группы:

Функции, возвращающие бесконечные итераторы count, cycle, repeat
Эти функции позволяют создавать из конечных коллекций бесконечные итераторы, то есть их элементы можно перебирать 
в бесконечном цикле.

count(start, step) — принимает на вход начальное значение (start, по умолчанию равно 0) и шаг (step, по умолчанию равен 1) 
бесконечно увеличивающейся числовой последовательности. В качестве значений аргументов можно использовать вещественные 
числа (float). Затем функция возвращает итератор, значения которого являются выходной последовательностью. 
Выведем числа от 0 до 1 с шагом 0.1. Так как возвращаемый итератор бесконечный, применим break для остановки цикла:
'''

from itertools import count

for value in count(0, 0.1):
    if value <= 1:
        print(round(value, 1))
    else:
        break

# 0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# 0.6
# 0.7
# 0.8
# 0.9
# 1.0

