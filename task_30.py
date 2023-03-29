# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an= a1 + (n-1) * d.
# Каждое число вводится с новой строки.

l=list()

n=int(input('Введите количество элементов массива: '))

start_elem=int(input('Введите первый элемент элемент массива: '))

diff_ar_prorgession=int(input('Введите разность арифметической прогрессии: '))

def list_ar_progr(list, size, start, diff):
    for i in range(1,size+1):
            a=start+(i-1)*diff
            list.append(a)
    return list

print(list_ar_progr(l,n,start_elem,diff_ar_prorgession))
