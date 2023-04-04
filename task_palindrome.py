# Проверить, является ли строка палиндромом.

def is_palindrome(text):
    if len(text)<=1:
        return True
    if text[0]==text[len(text)-1]:
        return is_palindrome(text[1:len(text)-1])
    else:
        return False
    

user_text=input('Введите строку: ')

print(is_palindrome(user_text))
