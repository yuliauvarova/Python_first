# Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string=input("Введите символы через пробелы: ")
list=string.split(" ")


d=dict()
string_new=""

for i in list:
    if i in d:
        d[i]+=1
        string_new = string_new + i + "_" + str(d[i]) + " "
    else:
        d[i]=0
        string_new = string_new + i + " "
    
print(string_new)

