print ('\n')
print ('Задание 1')
print ('\n')
c = 'Слово Буква'
print ('Исходное предложение' , c)
a , b = c.split()
a, b = b, a
result_1 = '! %s ! %s !' %(a,b)
result_2 = '! {} ! {} !'.format (a,b)
result_3 = f'! {a} ! {b} !'
print ('Новое предложение 1' , result_1)
print ('Новое предложение 2' , result_2)
print ('Новое предложение 3' , result_3)

print ('\n')
print ('Задание 2')
print ('\n')

print ('Привет! Правило игры: если надоело - напиши - break\n')
name = input ('Как вас зовут: ')
age = input ('Сколько вам лет: ')
while name and age !='':
    try:
        age = int (age)
        if name == 'break' or age == 'break':
            break
        elif int(age)<=0:
            print ('Ошибка. Повторите ввод\n')
        elif 0 < int(age) < 10:
            print (f'Привет, шкет, {name}\n')
        elif 10 <= int(age) <= 18:
            print (f'Как жизнь {name}?\n')
        elif 18 < int(age) < 100:
            print (f'Что желаете, {name}?\n')
        else:
            print (f'{name}, вы лжете - в наше время солько не живут...\n')
    except:
        print ('Ошибка. Операция завершена\n')
        break
    name = input ('Как вас зовут: ')
    age = input ('Сколько вам лет: ')

print ('\n')
print ('Задание 3')
print ('\n')    

number = input ('Введите целое число: ')
kub_1 = []
kub_2 = []
try:
    number_1 = int (number)
    while number_1 >= 0:
        kub_1.append (number_1 **3)
        number_1 -=1
    print (sorted(kub_1))
except:
    print ('Задание не выполнено, потому что не целое число')

try:
    number_2 = int (number)
    for i in range (0, number_2+1):
        kub_2.append (i**3)
    print (kub_2)
except:
    print ('Задание не выполнено, потому что не целое число')

print ('\n')
print ('Задание 4')
print ('\n')

user_name = input ('Как вас зовут: ')
import random 
chance = random.randint (1,10)
user_number = input (f'\nПривет, {user_name}, давай поиграем. Угадай число от 1 до 10. У тебя 3 попытки: ')
try:
    user_number == int (user_number)
    print ('\n--Дальше проверка на число отключена--')
    while user_number != '':
        if int(user_number) == int(chance):
            print ('\nМолодец, ты угадал число с первой попытки')
            break
        else:
            user_number = input ('\nНет. Твоя вторая попытка (число от 1 до 10) ')
            if int(user_number) == int(chance):
                print ('\nМолодец, ты угадал число со второй попытки')
                break
            else:
                user_number = input ('\nНет. Твоя последняя попытка (число от 1 до 10) ')
                if int(user_number) == int(chance):
                    print ('\nМолодец, ты угадал число с третьей попытки')
                    break
                else:
                    print ('\nGame over! Попытки закончились. Я загадала число ', chance)
                    break
except:
    print ('\nЗадание не выполнено, потому что не целое число')
