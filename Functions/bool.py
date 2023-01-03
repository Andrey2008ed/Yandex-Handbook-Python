# Класс bool Позволяет проверить/узнать логическое значение объекта.
# 1. Синтаксис:
#   bool(object)
# 2. Параметры:
#   object - любой объект, как строка, список, число и т. д.
# 3. Возвращаемое значение:
#   bool - логическое значение указанного объекта.
# 4. Описание:
#   Класс bool() возвращает логическое значение указанного объекта, True или False

# Объект всегда будет возвращать False, если:
#   Объект пуст - [], (), {}
#   Объект - False
#   Объект равен 0
#   Объект - None
# На практике редко вручную пользуются переменными типа bool, которые воспроизводятся логическими проверками, 
# потому что логические результаты автоматически используются инструкциями if ... else и другими средствами выбора.

#                   Примеры проверки объекта на его логическое значение.
x = bool(10)
print(x)
# Вывод
True

x = bool(0)
print(x)
# Вывод
False

x = bool([0])
print(x)
# Вывод
True

x = bool([])
print(x)
# Вывод
False

