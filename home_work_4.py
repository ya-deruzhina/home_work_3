print ('\n')
print ('Задание 1')
print ('\n')

import typing
dict_1 = {}
dict_1['one'] = 1
dict_1['two'] = 2
dict_1['tree'] = 3
print ('dict_1 = ', dict_1)
keys_dict_1 = list(dict_1.keys())
dict_2 = {}

def keys_for_dict (keys_dict_1 : typing.Optional [dict], dict_1 : typing.Optional [dict]) -> dict:
    if not keys_dict_1:
        return dict_2
    key_2 = dict_1 [keys_dict_1[0]]
    dict_2 [key_2] = keys_dict_1[0]
    keys_for_dict (keys_dict_1 [1:] , dict_1)

keys_for_dict(keys_dict_1,dict_1)        
print ('dict_2 = ', dict_2)    

print ('\n')
print ('Задание 2')
print ('\n')

factorial_res = [1]
def factorial (n : typing.Optional [int] , factorial_res : typing.Optional [list]) -> typing.Optional [int]:
    if n < 1:
        return factorial_res
    # print ('n = ' , n)
    factorial_res [0] *= n
    n-=1
    # print ('factorial_res = ', factorial_res)
    factorial (n, factorial_res) 

factorial (7 , factorial_res)
print ('factorial = ' , factorial_res)

print ('\n')
print ('Задание 3')
print ('\n')

list_for_work = list (input ('Введите число для подсчета: '))

repeat_number_dict = {}
repeat_number_dict ['0'] = 0
repeat_number_dict ['1'] = 0
repeat_number_dict ['2'] = 0
repeat_number_dict ['3'] = 0
repeat_number_dict ['4'] = 0
repeat_number_dict ['5'] = 0
repeat_number_dict ['6'] = 0
repeat_number_dict ['7'] = 0
repeat_number_dict ['8'] = 0
repeat_number_dict ['9'] = 0

# print(repeat_number_dict)
# print (list_for_work)
def repeat_number (list_for_work : typing.Optional[list]) -> typing.Optional[list]:
    if not list_for_work or int(list_for_work[0]) < 0:
        print ('\nПодсчет закончен. Функция прекращает работу\n')
        return repeat_number_dict
    elif int(list_for_work[0]) == 0:
        repeat_number_dict ['0'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 1:
        repeat_number_dict ['1'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 2:
        repeat_number_dict ['2'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 3:
        repeat_number_dict ['3'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 4:
        repeat_number_dict ['4'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 5:
        repeat_number_dict ['5'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 6:
        repeat_number_dict ['6'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 7:
        repeat_number_dict ['7'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 8:
        repeat_number_dict ['8'] +=1
        repeat_number (list_for_work[1:])
    elif int(list_for_work[0]) == 9:
        repeat_number_dict ['9'] +=1
        repeat_number (list_for_work[1:])

repeat_number (list_for_work)
print (repeat_number_dict)    

print ('\n')
print ('Задание 4')
print ('\n')

from datetime import datetime

key_format = input ('\nВведите число, сколько данных нужно отображать \n 1 - только секунды,\n 2 - минуты, секунды, \n 3 - час, минуты, секунды, \n 4 - день, час, минуты, секунды, \n 5 - месяц, день, час, минуты, секунды, \n 6 - год, месяц, день, час, минуты, секунды). \n\n Итак, какой формат выбрали? ')
format_data = {'1': '%S' , '2': '%M:%S' , '3':'%H:%M:%S' , '4':'%d %H:%M:%S' , '5':'%m-%d %H:%M:%S' , '6':'%Y-%m-%d %H:%M:%S'}
data = datetime.strftime(datetime.now(),format_data[key_format])
print ('Время: ' , data)
def data_time (num , key_format , format_data , data ):
    data_future = data [:-1] + str((int (data [-2:-1])) + num)
    return data_future

print ([data_time (item , key_format , format_data, data ) for item in range(5)])