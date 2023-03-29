# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'


n = int(input())
print(f(n))