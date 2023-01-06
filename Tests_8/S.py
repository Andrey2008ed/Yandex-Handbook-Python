"""
Таблица истинности 2

Продолжим работу с таблицами истинности. Продумайте программу, которая для введённого сложного 
логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных валидное для языка Python.

Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
В выражении все переменные заданы заглавными латинскими буквами.
Обратите внимание на параметры __globals и __locals у функции eval.

Ввод:
not A or B and C

Вывод:
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 0
1 1 1 1
"""

import itertools
import re

# Примеры внутри функции основаны на выражениях:
# 1) not A or B and C
# 2) A and not B and A

def build_truth_table(expression):
    """Функция для построения таблицы истинности для любого выражения"""

    # Получить множество всех переменных в выражении
    variables = set(re.findall('[A-Z]', expression))
    # 1) {A, C, B}
    # 2) {B, A}

    # Отстортировать множество в лексикографическом порядке
    variables = sorted(variables)
    # 1) {A, B, C}
    # 2) {A, B}

    # Создать список всех возможных комбинаций значений 0 и 1 для этих переменных
    combinations = list(itertools.product([0, 1], repeat=len(variables)))
    # 1) [(0,0,0), (0,0,1), (0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
    # 2) [(0,0), (0,1), (1,0), (1,1)]

    # Создать список всех возможных значений выражения для этих комбинаций
    values = []
    for combination in combinations:

        # Преобразовать комбинацию в словарь, где каждая переменная соответствует своему значению
        variables_values = dict(zip(variables, combination))
        # Для первой комбинации словари выглядят так:
        # 1) {"A": 0, "B": 0, "C": 0}
        # 2) {"A": 0, "B": 0}

        # Подставить эти значения в выражение и вычислить результат
        value = eval(expression, variables_values)
        # value проверит комбинацию полученную из variables_values на истинность согласно выражению
        # 1) not A or B and C для {"A": 0, "B": 0, "C": 0}
        # 2) A and not B and A для {"A": 0, "B": 0}

        # Результат истинности выражения сохраняем в список values
        values.append(value)
    
    # Вернуть результат в виде таблицы
    return variables, combinations, values


# Считать выражение с консоли
expression = input()
# Построить таблицу истинности (Получить значения этих переменных на основании работы функции)
variables, combinations, values = build_truth_table(expression)

# Вывести таблицу истинности
print(" ".join(variables) + " F")
# A B C F
for combination, value in zip(combinations, values):
    print(" ".join(str(x) for x in combination) + " " + str(int(value)))
    # 0 0 0 True
    # Для того, чтобы избежать True при выводе, необходимо привести значение value к int. Тем самым получив 1 или 0
