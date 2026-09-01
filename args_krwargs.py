def fn (*args): 
    print(args)  ## this will print the tuple of arguments passed to the function.
    print(type(args))  ## this will print the type of args which is tuple.
    for i in args:
        print(i)  ## this will print each argument passed to the function.



fn(1,2,3,4,5)  ## this will print the tuple of arguments passed to the function.


def fn1(*args, **kwargs): 
    print(args)  ## this will print the tuple of arguments passed to the function.
    print(type(args))  ## this will print the type of args which is tuple.
    for i in args:
        print(i)  ## this will print each argument passed to the function.
    
    print(kwargs)  ## this will print the dictionary of keyword arguments passed to the function.
    print(type(kwargs))  ## this will print the type of kwargs which is dictionary.
    for key, value in kwargs.items():
        print(key, value)  ## this will print each key-value pair in the dictionary.


fn1(1,2,3,4,5, name="aryan", age=20)  ## this will print the tuple of arguments and dictionary of keyword arguments passed to the function


dict = {"name": "aryan", "age": 20}  ## this is a dictionary with key-value pairs.
print(dict.items())