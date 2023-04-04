# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

values = [0, 2, 8, 6, 10] 

def same_by (characteristic, list):
    i=0
    while i <len(list):
        if characteristic(list[i])==characteristic(list[i-1]):
            i+=1
        else:
            return False
    return True
      

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

