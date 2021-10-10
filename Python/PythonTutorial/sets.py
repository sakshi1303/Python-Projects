# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:50:16 2020

@author: Sakshi Agarwal
"""

basket = {'orange', 'apple', 'mango', 'apple', 'orange'}
print(type(basket))
print(basket)

a = set()
a.add(1)
a.add(2)
a.add(2)
print(a)

##print(a[0])

numbers=[1,2,3,4,2,3,4]
uniq_num = set(numbers)
print(uniq_num)


fs = frozenset(numbers)
print(fs)
##fs.add(5) ##It will give error


x = {'a','b','c'}

print('a' in x)
print('d' in x)

for i in x:
    print(i)
    
    
y ={'a','g','h'}
print(x|y)
print(x&y)    
print(x-y)
print(x<y)
x={'h','g'}
print(x<y)

    
    