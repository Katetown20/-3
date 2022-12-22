# задача 1
l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
l_1 = []
for i in l:
    if i not in l_1:
        l_1.append(i)
    else:
        print(i, end=' ')

# задача 2
from random import randint
n = 5
lst = []
mat = [[randint(0,100) for i in range(n)] for j in range(n)]
for i in range(n):
    print(mat[i])
for i in range(n):
    m_a_x = max(mat[i])
    print(m_a_x)
    lst.append(m_a_x)
lst_max = max(lst)
print(lst)
print(lst_max)

# задача 3
dic = {'name':'id1', 'name2':'id2', 'name3':'id3'}
new_dic = {value: key for key, value in dic.items()}
print(dic)
print(new_dic)

