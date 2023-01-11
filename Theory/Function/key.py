"""
В одной из прошлых глав мы изучили функцию sorted(), которая возвращает отсортированный список, 
состоящий из элементов переданного ей итерируемого объекта. По умолчанию критерием сортировки 
являются значения элементов. 

То есть сравниваются числа, строки по положению символов в таблице 
кодировки и так далее. У данной функции есть возможность задать критерий сортировки, передав в 
именованный аргумент key функцию, по значениям которой будет производиться сортировка.

Напишем программу для сортировки списка строк по длине строки в порядке возрастания:
"""

lines = ["abcd", "ab", "abc", "abcdef"]
print(sorted(lines, key=lambda line: len(line)))
# ['ab', 'abc', 'abcd', 'abcdef']


"""
Для задания функции-критерия сортировки была использована лямбда-функция.

С помощью аргумента key можно задать несколько критериев сортировки одновременно. 
Для этого в лямбда-функции нужно вернуть кортеж значений в порядке приоритета критериев. 

Напишем программу, которая сортирует список строк, состоящих из строчных букв латинского 
алфавита, по возрастанию длины, а если длина одинакова, то по алфавиту.
"""

lines = ["abcd", "ab", "ba", "acde"]
print(sorted(lines, key=lambda line: (len(line), line)))
# ['ab', 'ba', 'abcd', 'acde']



"""
Если по числовому критерию (например, длина строки) нужно поменять направление сортировки, то 
можно просто поставить минус перед возвращаемым значением в лямбда-функции. 
Отсортируем список строк по убыванию длины, а если длина одинакова, то по алфавиту:
"""

lines = ["abcd", "ab", "ba", "acde"]
print(sorted(lines, key=lambda line: (-len(line), line)))
# ['abcd', 'acde', 'ab', 'ba']



"""
Аргумент key есть и у метода sort() (меняет исходный список на отсортированный), а также у 
функций max() и min(). Найдем в списке строк самую длинную, а если таких несколько, то лексикографически меньшую:
"""

lines = ["abcd", "ab", "ba", "acde"]
print(min(lines, key=lambda line: (-len(line), line)))
# abcd



"""
Если вспомнить про списочные выражения, то функции map() и filter() можно заменить 
соответствующими списочными выражениями. Например:
"""

result = (x for x in [-1, 5, 6, -10, 0] if x > 0)
print(", ".join(str(x) for x in result))
# 5, 6




