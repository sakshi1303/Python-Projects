""" Basic Generator

def remote_control():
    yield "CNN"
    yield "ESPN"
    
print("Using Iterator..")    
itr = remote_control()  
print(next(itr))
print(next(itr))

print("Using Loop..")
for c in remote_control():
    print(c)
    
"""

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
        

for f in fib():
    if f > 50:
        break
    print(f)
        
        