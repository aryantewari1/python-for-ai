##functools is an important module that lets us achieve multiple things by the help of modules

##1. Partial. 

##Partials takes a function and returns a new function with some argument pre-filled. 
## the basic syntax is partial(function, fixed_arguments)


from functools import partial, lru_cache, singledispatch 

def powerFun(base, exponent): 
    return base**exponent

cube = partial(powerFun, exponent = 3)


print(cube(3))


##2 Lru_cache --> helps in achieving memoization 
## sometimes some functions will take ages to perform the computation
## so what you like in those cases is that just skip the computation 
## in that case you cache those responses yes.. memory is compromised 
## but memory is secondary because speed is achieved 

## practical example would be api calls taking long so just cache the response 
## next time it wont take as long. 

@lru_cache(maxsize=None) ## define the max size of cache u want. 
## max size controls how many recent calls are cached otherwise least recent used gets evicted firs.
def fib(n): 
    if n==0 or n ==1 : return n 
    return fib(n-1) + fib(n-2)

print(fib(55))

## the problem with fib is it will repeat computations to get u the result 
## this is fine as long as the function calls are small 
## this becomes difficult as soon as the function calls largens up
## to avoid we use memoization achieved as shown.