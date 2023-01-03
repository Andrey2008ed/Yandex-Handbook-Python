# При использовании оператора break во вложенных циклах он останавливает только тот цикл, в котором непосредственно вызывается.
# Дополним первый пример с генерацией двухбуквенных строк условием: сгенерировать последовательно двухбуквенные строки по 
# алфавиту до строки «ya».

flag = False
for i in range(26):
    for j in range(26):
        text = f"{chr(ord('a') + i)}{chr(ord('a') + j)}"
        if text == "ya":
            print(text)
            flag = True
            break
        print(text)
    if flag:
        break

# В программе по-прежнему используются вложенные циклы. Генерация и вывод происходят без изменений. 
# Обратите внимание на переменную-флаг flag логического (булева) типа. Она нужна для сигнала, что программа дошла до 
# заданной комбинации букв и требуется остановить внешний цикл, так как break во внутреннем цикле остановит только 
# внутренний цикл.

# Обычно флаг устанавливают в начальное значение False (флаг опущен), а при выполнении какого-то условия в программе 
# флаг устанавливают в значение True (флаг поднят). При генерации комбинации «ya» происходит вывод этой комбинации, 
# «поднятие» флага и остановка внутреннего цикла. После завершения внутреннего цикла происходит проверка состояния флага,
# и если флаг поднят, то останавливается и внешний цикл.

