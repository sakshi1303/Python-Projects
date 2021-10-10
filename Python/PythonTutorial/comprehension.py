print('List Comprehension..')

numbers = [1,2,3,4,5,6,7]
even=[]

print('Using Loop..')
for i in numbers:
    if i%2 == 0:
        even.append(i)

print(even)

print('Using Comprehension..')
even = [i for i in numbers if i%2 == 0]        
print(even)

sqr_numbers = [i*i for i in numbers]
print(sqr_numbers)

print('Set Comprehension..')

s = set([1,2,3,4,5,2,1])
print(s)

even_num  = {i for i in s if i%2 == 0 }
print(even_num)

print('Dictionary Comprehension..')

cities = ['Mumbai', 'New York', 'Paris']
countries = ['India', 'USA', 'France']

z = zip(cities, countries)
z

for a in z:
    print(a)
    
    
d = {city:country for city,country in zip(cities, countries)}    
print(d)