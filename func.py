def fn_name(): 
    print("This is a function")

## *args creates a tuple just like ...args does in js 

def func(*args):
    for i in args:
        print(i)


func(1,2,3,4,5)
##lambda expressions 

to_square =lambda x:x**2 
print(to_square(2))
to_upper = lambda x: x.upper()
print(to_upper("hello"))