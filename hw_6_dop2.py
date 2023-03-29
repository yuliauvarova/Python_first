# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

l1=list()

for i in range(10,100):
    l1.append(i)
        
print(l1)

def fun_filter(i):
    if i%9==0:
        return True
    else:
        return False

filtered = filter(fun_filter, l1)

print('Делятся на 9:')
for s in filtered:
    print(s)

def pow_2(a):
    return a*a

result=map(pow_2,l1)

l2=list(result)

sum_result=sum(l2)

print()

print(sum_result)


