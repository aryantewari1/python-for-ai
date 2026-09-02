##Functions are first class objects in python, 
## just like javascript, but the only catch is you dont have arrow functions so you cannot define 
## the body of the function in the call itself..

##1. functions can be assigned to any variable 

x = lambda x: x*x 
print(x(5))


##2 functions can return functions

def multiply(n): 
    def multiplier(x): 
        return x*n ##closures. 

    return multiplier 


times3 = multiply(3) 
print(times3(3))

##3 functions can be passed as argument.


## this is basically the map function
def does_something_to_list(list, func):
    new_list = []
    for x in list:
        new_list.append(func(x))

    return new_list

my_list = does_something_to_list([1,2,3,4], lambda x: x*x*x) 
print(my_list) 

##functions are objects in themselves.

def does_nothing(): 
    x=5
    """this function does literally nothing"""
    pass

print(type(does_nothing)) ##class of type 'function' 
print(does_nothing.__dict__)
print(does_nothing.__doc__)
print(does_nothing.__name__)