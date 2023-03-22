#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

letters1=["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
a={letters1[i]:1 for i in range(len(letters1))}

letters2=["D", "G","Д", "К", "Л", "М", "П", "У"]
b={letters2[i]:2 for i in range(len(letters2))}

letters3=["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"]
c={letters3[i]:3 for i in range(len(letters3))}

letters4=["F", "H", "V", "W", "Y", "Й", "Ы"]
d={letters4[i]:4 for i in range(len(letters4))}

letters5=["K", "Ж", "З", "Х", "Ц", "Ч"]
e={letters5[i]:5 for i in range(len(letters5))}

letters8=["J", "X", "Ш", "Э", "Ю"]
f={letters8[i]:8 for i in range(len(letters8))}

letters10=["Q", "Z", "Ф", "Щ", "Ъ"]
g={letters10[i]:10 for i in range(len(letters10))}

a.update(b)
a.update(c)
a.update(d)
a.update(e)
a.update(f)
a.update(g)


word=input("Введите одно слово: ")
sum=0
word=word.upper()
print(word)

for i in word:

    sum=sum+a[i]
    

print(sum)