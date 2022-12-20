#задача 1-3
import json

regist = {}

# функция регистрации + проверка на уже зарегистрированность
def registration(login, password):

    # проверка на зарегистрированность
    with open('reg.json', 'r') as f:
        regist = json.load(f)

    if login in regist.keys():
        print('Пользователь с таким логином уже существует')

    # если такого логина нет, происходит регистрация
    else:
        regist[login] = password
        with open('reg.json', 'w') as f:
            json.dump(regist, f)
        return print('Вы успешно зарегистрированны!')

# функция проверяющая правильность введённого логина или пароля
def entering(login, password):

    with open('reg.json', 'r') as f:
        regist = json.load(f)

    if login in regist.keys() and regist[login] == password :
        print('Вы успешно вошли')

    elif login not in regist.keys():
        print('Пользователь с таким логином на найден')

    else:
        print('Вы ввлели неверный логин или пароль')

while True:

    logining = str(input('Вход или регистрация? '))
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    if logining =='вход':
        entering(login, password)

    elif logining == 'регистрация':
        registration(login, password)