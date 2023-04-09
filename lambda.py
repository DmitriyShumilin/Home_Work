#Отфильтруйте список строк, чтобы остались только буквы!

# list_ = ['Dima 33', 'Yulia 38', 'Artem 3']
# list = list(map(lambda x: ''.join([letter for letter in x if letter.isalpha()]), list_))
# print(list)


#Посчитайте среднее арифмитическое чисел!

#from functools import reduce
#list_ = [10, 20, 30, 40]
#lst_2 = reduce(lambda x, y: x + y, list_)/len(list_)
#print(lst_2)

#Список людей, добавить возраст, исходя из года рождения.

#persons = [{'name': 'Vasia', 'birth_year':1999},
          #{'name': 'Petr', 'birth_year':2005}]
#list_ =list(map(lambda dict_: dict_.update ({'age': 2023 - dict_['birth_year']}), persons))
#print(persons)

#Декоратор для функции:


#def wrapper(func):  # декоратор (wrapper=>обертка) - это функция, которая принимает в себя другую функцию (func) в нашем случае это функция (test)
    #def inner():  # inner - это внутренняя (вложенная) функция в наш декоратор (wrapper) -> в которой будет изменяться поведение нашей функции (test)
        #name = func()  # переменной name, присваиваем значение, принятое нашим декоратором (wrapper) т.е. то, что ввел пользователь
        #name = name.capitalize()  # переопределяем значение нашей переменной name, применяя к ней метод (capitalize())
        #print(name)  # выводим полученное значение, нашей переопределенной переменной name
   # return inner  # и декоратор (wrapper=>обертка) => возвращает другую функцию (inner) т.е. возвращает значение, полученное в результате отработки кода в вложенной функции inner


#@wrapper
#def test():
   #return input('Введите имя: ')


#test()









