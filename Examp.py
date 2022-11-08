def is_that_number(mes):               # Позволяет ввести с коносоли вещественное число (кроме 0), возвращая
  print(mes)                           # пользователя ко вводу каждый раз, если ввод не корректен
  val = input('=>  ')
  try:
    if float(val) == 0:
        raise Exception("\033[1;31mЧисло не должно быть равно 0\033[0m")
    return float(val)    
  except ValueError:
    print('\033[1;31mЭто не число!\033[0m')  
    return is_that_number(mes)
  except Exception as e:
    print(e)
    return is_that_number(mes)

def inp_ut(x):
    while True:
        try:
            text = '{} {} {} '.format("Введите, пожалуйста,число",x,'>>>')
            a = float(input(text))
            return a
        except ValueError:
            print("Please reinsert")
 
a = inp_ut('a')
b = inp_ut('b')
c = inp_ut('c')