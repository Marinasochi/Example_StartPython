# Обычные операторы <, <=, >, >=, ==, != неравенство 
a = 5 < 4                                  # Это неравенство не верное
print(a)                                   # На экран выводится - False
d = 'sad' == 'sad'                         # Строки также можно сравнивать
print(d)                                   # True
g = 'cat' == 'tad'                         # Очевидно, что не равны
print(g)                                   # False
u = [2, 3, 4, 5]                           # Объявление списка
v = [8, 6, 10, 0]                          # - || -
y = [8, 6, 10, 0]                          # - || -
print(v[3], y[0])                          # Вывод на экран 0, 8 - соттветствующие элементы списков v и u
print(u == v)                              # False
print(y != v)                              # False
b = 7 < 8 > 10 > 1 < 3 > 2                 # Можно использовать множественные неравенства
print(f'Это неравенство {b}!')             # Это неравенство False!
# not, and, or, is, is not, in, in not
e = 7 < 3 or 5 > 2                         # Присваивание значения переменной e
s = not d == g                             # - ||- ы
print(e, s)                                # True, True
print(6 is y)                              # False (6 не является списком у)
print(8 and 6 in y and 2 in u)             # True (8 и 6 содержатся в у, 2 содержится в списке u)
print(((7 and 10) in y) and ((5 and 8) in v)) # True, хотя очевидно, что это ложь: in работает только 
                                           # для одного числа в данной записи
print(8, 6, 10 in y)                       # 8,6 True
print((8, 6, 10) in y)                     # False нужно использовать такую запись!!!   
print(type(u))                             # list - узнаем какой тип данных
c = range(1, 8)                            # генерация последовательности от 1 до 8 с шагом 1
for i in c:                                # вывод последовательности с на печать
 print(i, end = ' ')                       # 1 2 3 4 5 6 7 end позволяет печатать в одну строку с указанием разделителя, в данном случае пробела  
print()
c = list(c)
print(type(c)) 