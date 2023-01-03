a = [x, s, t, n, i] = 0


x in s
# Возвращает True, если в списке s есть элемент x. Иначе False
1 in [1, 2, 3]
# True

x not in s
# Возвращает False, если в списке s есть элемент x. Иначе True
4 not in [1, 2, 3]
# True

s + t
# Возвращает список, полученный конкатенацией списков s и t
[1, 2] + [3, 4, 5]
# [1, 2, 3, 4, 5]

s * n (n * s)
# Возвращает список, полученный дублированием n раз списка s
[1, 2, 3] * 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

len(s)
# Возвращает длину списка s
len([1, 2, 3])
# 3

min(s)
# Возвращает минимальный элемент списка
min([1, 2, 3])
# 1

max(s)
# Возвращает максимальный элемент списка
max([1, 2, 3])
# 3

s.index(x)
# Возвращает индекс первого найденного элемента x. Вызывается исключение ValueError, если элемент не найден
[1, 2, 3, 2, 1].index(2)
# 1

s.count(x)
# Возвращает количество элементов x
[1, 1, 1, 2, 3, 1].count(1)
# 4

s.append(x)
# Добавляет элемент x в конец списка
s = [1, 2]
s.append(3)
# [1, 2, 3]

s.clear()
# Удаляет все элементы списка
s = [1, 2, 3]
s.clear()
# []

s.copy()
# Возвращает копию списка
[1, 2, 3].copy()
# [1, 2, 3]

s.extend(t) 
# Расширяет список s элементами списка t
s = [1, 2, 3]
s.extend([4, 5])
# [1, 2, 3, 4, 5]

s.insert(i, x)
# Вставляет элемент x в список по индексу i
s = [1, 3, 4]
s.insert(1, 2)
# [1, 2, 3, 4]

s.pop(i)
# Возвращает и удаляет элемент с индексом i. Если i не указан, то возвращается и удаляется последний элемент
s = [1, 2, 3]
x = s.pop()
# x = 3
# s = [1, 2]

s.remove(x)
# Удаляет первый элемент со значением x
s = [1, 2, 3, 2, 1]
s.remove(2)
# [1, 3, 2, 1]

s.reverse()
# Меняет порядок элементов списка на противоположный (переворачивает список)
s = [1, 2, 3]
s.reverse()
# [3, 2, 1]

s.sort()
# Сортирует список по возрастанию, меняя исходный список. 
# Для сортировки по убыванию используется дополнительный аргумент reverse=True
s = [2, 3, 1]
s.sort()
# [1, 2, 3]

sorted(s)
# Возвращает отсортированный по возрастанию список, не меняя исходный. 
# Для сортировки по убыванию используется дополнительный аргумент reverse=True
s = [2, 3, 1]
new_s = sorted(s, reverse=True)
# [3, 2, 1]







