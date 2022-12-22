# задача 1
import math#
a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))#
c = float(input('Введите сторону c: '))

def triangle(a,b,c):
    p = (a + b + c)/2
    s = math.sqrt(p * (p-a) * (p-b) * (p-c))
    return print('Площадь треугольника равна: ', s)

triangle(a,b,c)

# задача 2
s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

word_list = []

sunb_1 = ','
for i in s:
    if i in sunb_1:
        s = s.replace(i, '')

sunb_2 = '.'
for i in s:
    if i in sunb_2:
        s = s.replace(i, '')

sunb_3 = '...'
for i in s:
    if i in sunb_3:
        s = s.replace(i, '')

sunb_4 = '-'
for i in s:
    if i in sunb_4:
        s = s.replace(i, '')

sunb_5 = '!'
for i in s:
    if i in sunb_5:
        s = s.replace(i, '')


s_list = s.split()

def short_word(s):
    for i in s_list:
        if len(i) < 5:
            word_list.append(i)
            word = ', '.join(word_list)
    return print(word)

short_word(s)

# задача 3
l= [56, 9, 11,2]
#l = [61,228,9]
def join(l):
    print(''.join((sorted([str(x) for x in l], reverse=True))))

join(l)

