## 0, 1, 1, 2, 3, 5 ,8

## function for the nth term of fibonacci. 

def fib(n): 
    a,b = 0,1
    if n == 0: return n 
    if n == 1: return n

    while n-2>0: 
        val = b 
        b = a+b 
        a = val
        n=n-1
    return b 


print(fib(2)) 
print(fib(6))