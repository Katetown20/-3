# задача 1
x = float(input('Введите сумму вклада: '))
p = float(input('Процентная ставка вклада: '))
y = int(input('Ожидаемая сумма: '))

count = 0
while x < y:
    x = round(((p * x)/100)+x)
    count += 1
print('Ожидаемая сумма вклада будет достигнута через: ', count, 'года')

# задача 2
n = int(input('Введите число повторений: '))
count = 0
while count != n:
    print('for частный случай цикла while')
    count +=1

# задача 3
num = int(input('Введите число: '))
suma = 0
while num > 0:
    dig = num % 10
    suma = suma + dig
    num = num // 10
print('Сумма введённых чисел равна:', suma)