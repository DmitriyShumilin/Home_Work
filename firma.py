age = float(input('Ваш возраст'))
if 20 <= age:
   print('Сотрудник подходит')
else:
   print('Сотрудник не подходит')
st = int(input('Стаж работы:'))
if 3 <= st:
   print('Сотрудник подходит')
else:
    print('Сотрудник не подходит')
    #Пользователь вводит номер месяца, приложение сообщает, какое это время года:
num = input ('Введите номер месяца')
if num == 3 or 4 or 5:
    print ('Весна')
elif num == 6 or 7 or 8:
    print ('Лето')
elif num == 9 or 10 or 11:
    print ('Осень')
elif num == 12 or 11 or 2:
    print ('Зима')
