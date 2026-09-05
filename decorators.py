##Decorators are essentially functions which take up a function
## add functionality to it and return a new function to you

def my_decorator(func):
    def wrapper():
        print("this line is added")
        func()
        print("this line ends")

    return wrapper



## python has a better way of doing this thing 
## instead of doing that 
@my_decorator
def greet(): 
    print("hello to a new world")

greet()

## what if the func being passed has arguments 

def decorator_but_args(func):
    def wrapper(*args, **kwargs): ## passing args and kwargs
        ##because eventually wrapper hi call hoga and uske andr func
        print('hello')
        func(*args,**kwargs) #here its unwrapping 

    return wrapper

@decorator_but_args
def add(a,b): 
    print("result is:" , a+b)

add(3,2)

## How long func takes for argument 

import time 

def decorator_time(func): 
    def wrapper(): 
        start = time.time() 
        func()
        end = time.time()

        print(f"function took {start-end} seconds to execute")

    return wrapper 


@decorator_time
def delayed_func():
    time.sleep(1)
    print("i took 1 second")


delayed_func()


##functool.wraps :- since its the wrapper function which gets returned
##so essentially you are handling wrapper functioon and not the original func
## to ensure the func remains evident still after wrap
## we can use wraps

from functools import wraps 


def decorator_amazing(func):
    @wraps(func)
    def wrapper():
        print("this is a wrapper")
        func()
        print("the wrapper ends")
    return wrapper


@decorator_amazing
def orig_Func():
    """this is the doc string of original func"""
    print("wow") 


print(orig_Func.__name__)
print(orig_Func.__doc__)