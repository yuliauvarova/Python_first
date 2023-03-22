# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text=input("Введите текст: ")
text=text.lower()
list=text.split(" ")
print(list)

a=set()

for v in list:
    v=v.replace(' ','')
    if v!="":
        a.add(v)

print(a)

count=0

for i in a:
    count+=1

print(count)

# text = input('Введите текст: ')

# text_set = set(text.lower().split())
# print(len(text_set))