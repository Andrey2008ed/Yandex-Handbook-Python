# Выведем на экран целые чётные числа в диапазоне от 0 до n (n вводится пользователем):

n = int(input("Введите конец диапазона: "))
for i in range(0, n + 1, 2):
    print(i)