# Используя в функции range() отрицательный шаг, можно запустить цикл в обратном порядке:

n = int(input("Введите количество чисел: "))
for i in range(n, -1, -1):
    print(i)