# Проверить, является ли строка палиндромом.

def is_palindrome(text):
    if len(text)<=1:
        return 'yes'
    if text[0]==text[len(text)-1]:
        is_palindrome(text[1:len(text)-1])
        return 'yes'
    else:
        return 'no'
    

user_text=input('Введите строку: ')

print(is_palindrome(user_text))
