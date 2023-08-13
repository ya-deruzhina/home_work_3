from datetime import datetime
from functools import reduce

print ('\n')
print ('Задание 1')
print ('\n')

list_1 = [11,12,13,14,15,16,17,88,99,110,112,1221,131]
list_2 = list_1[:]
print('list_1 = list_2 = ' , list_2)
print (list(map(lambda i: 'четное' if (i % 2 == 0) else 'нечетное',list_2)))

print ('\n')
print ('Задание 2')
print ('\n')

list_3 = list_1[:]
print('list_1 = list_3 = ' , list_3)
list_4 = (list(map(lambda i: (i :=str(i)),list_3)))
print(list_4)

print ('\n')
print ('Задание 3')
print ('\n')

tuple_1 = tuple (list_4)
print('tuple_1 = ' , tuple_1)
print (list(filter(lambda b: b == (''.join(reversed (str(b)))) , tuple_1)))

print ('\n')
print ('Задание 4')
print ('\n')

def decor_1 (func_1):
    def wrapper (k):
        time_1 = datetime.now()
        print (time_1)
        a = 1000**999999
        func_1 (k)
        time_2 = datetime.now()
        print (time_2)
        print ('Время выполнения функции ', time_2 - time_1)
    return wrapper

@decor_1
def calculator_1 (list_1: list):
    reduce(lambda b, c: (b+c)*2, list_1)
           
calculator_1 (list_1)

def decor_2 (func_2):
    def wrapper (t):
        time_1 = datetime.now()
        print (time_1)
        a = t**2
        func_2 (t)
        time_2 = datetime.now()
        print (time_2)
        print ('Время выполнения функции ', time_2 - time_1)
    return wrapper

@decor_2
def calculator_2 (list_1: list):
    reduce(lambda b, c: (b+c)*2, list_1)
           
calculator_1 (list_1)

print ('\n')
print ('Задание 5')
print ('\n')

def eto_stroka (str_1):
    try:
        str_1 = float (str_1)
        if str_1 < 0:
            if str_1 % 1 !=0:
                print ('Вы ввели отрицательное дробное число ', str_1)
            else:
                print ('Вы ввели отрицательное целое число ', str_1)
        else:
            if str_1 % 1 !=0:
                print ('Вы ввели положительное дробное число ', str_1)
            else:
                print ('Вы ввели положительное целое число ', str_1)
    except:
        print ('Вы ввели некорректное число' , str_1)


# eto_stroka()
eto_stroka (str(1))
eto_stroka (str(10))
eto_stroka (str(1.5))
eto_stroka (str(-1))
eto_stroka (str(-10))
eto_stroka (str(-1.5))
eto_stroka (str(0))
eto_stroka (str('10v'))
eto_stroka (str('1.5d'))