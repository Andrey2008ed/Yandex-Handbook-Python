# Выведем на экран целые числа в диапазоне от k до n - 1 (k, n вводятся пользователем):

k = int(input("Введите начало диапазона: "))
n = int(input("Введите конец (без включения) диапазона: "))
for i in range(k, n):
    print(i)
