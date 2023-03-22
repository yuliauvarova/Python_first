# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

import random

n=int(input("Введите длину массива: "))

list1=[]
i=0
while i<n: 
    list1.append(random.randint(-10,10))
    i+=1

print(list1)

count=0

for i in range(len(list1)-1):
    if list1[i+1]>list1[i]:
        count+=1

print()
print(count)
