# Функция chr() в Python, число в символ Юникода.
# 1. Синтаксис:
#   chr(x)
# 2. Параметры:
#   x - целое число int в диапазоне - от 0 до 1114111 (0x10FFFF в базе 16).
# 3. Возвращаемое значение:
#   str - строкa, представляющая символ Unicode.
# 4. Описание:
# Функция chr() вернет строку, представляющую символ, соответствующий переданному в качестве аргумента целому числу из 
# таблицы символов Unicode. Например, chr(97) возвращает строку a, а chr(8364) возвращает строку €. 
# Функция chr() - обратная функции ord().

ord('A')
# 65
chr(65)
# 'A'

# Допустимый диапазон аргументов - от 0 до 1114111 (0x10FFFF в базе 16).
# Будет поднят ValueError, если x за пределами этого диапазона.
# Если необходимо преобразовать символ в число из таблицы символов Unicode, то используйте функцию ord().

#                   Примеры преобразований чисел в символы Юникода.
chr(97)
# a'
chr(10)
'\n'

# числа из таблицы символов Unicode
for el in range(49, 58):
    print(chr(el))
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9