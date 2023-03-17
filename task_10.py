# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random

n=int(input("Введите число монет: "))
count_tails=0
count_eagle=0

for i in range(n):
    temp=random.randint(0,1)
    print(temp)
    if temp==0:
        count_tails+=1
    elif temp==1:
        count_eagle+=1

print()

print(count_tails) if count_tails<count_eagle else print(count_eagle)
