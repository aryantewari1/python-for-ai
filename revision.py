x = 5
print(type(x))

list = [1, 2, 3, 4, 5]
print(list)

## tuple -  an immutable ordered collection of elements 

## you cannot change the values inside any tuple once it is created. it is immutable. ( ) 


##String - 

## dictionary is like objects in JavaScript. It is a collection of key-value pairs. 

dict = {
    "name": "John",}
print(dict);
print(dict["name"])


## f string - if you want to use variables inside a string, you can use f-string. dynamically

name = "Alice" 
age = 30 

print("My name is {} and i am {} years old".format(name,age))
print(f"My name is {name} and i am {age} years old")



## strings 


str = "hello world" 

print(str[0:3])
print(str.upper())
print(str.capitalize())
print(str.title())

## in python we dont have trim() we have strip(), if trailing spaces are there u can use strip()

str2 = "     hello world     "
print(str2.strip())

str3 = "hello-world-python-zindabad"
arr = str3.split("-")
print(arr)
str4 = ",".join(arr)
print(str4)


## loop , conditionals 

for i in range(0,3):
    print(i)


for i in range(0,len(arr)):  ## this is how we do it in other languages. 
    print(arr[i])


print("python" in arr) 


condition = True;
count = 0
while(condition and count!=5):
    print("this is a while loop")
    count+=1

n =4 
match n: 
    case 1 | 4: print(1) 
    case 2: print(2)
    case 5: print(" you have hit the jackpot")
    case _: print("hey you didnt provide the right number")


## kwards 

def printNameandAge(**kwargs): 
    print(kwargs["name"])
    print(kwargs["age"])
    return 8, 10,22
printNameandAge(name="aryan", age=18) 

## lambda expressions are like one line anonnymous functions!! !


value1 = lambda x: x**2
print(value1(2))
