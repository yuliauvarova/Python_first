# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X

import random

import math

n=int(input('Введите количество элементов в массиве: '))

a=[]
i=0
for i in range(n):
    a.append(random.randint(-10,10))
    print(a[i])
    i+=1

print()

count=0
i=0
diff=0
mindiff=a[0]-a[-1]
mindiff_index=0

while i<n-1:
    diff=abs(a[i]-a[-1])
    if diff<mindiff:
        mindiff_index=i
    i+=1

print(a[mindiff_index])