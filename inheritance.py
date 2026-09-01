# class Animal: 
#     pass

# class Dog(Animal):
#     def speak(self): return "Bark"
# class Cat(Animal):
#     def speak(self): return "Meow"

# animals = [Dog("Rex"), Cat("Tom")]
# for a in animals:
#     print(a.speak())

##super() is a function that allows you to call methods from the parent class.


class Shape:
    def __init__ (self,name):
        self.name = name

    def removeShape(self): 
        print(f"{self.name} has been removed")


class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def area(self):

        return self.side_length ** 2

    def removeShape(self):
        super().removeShape()
        print(f"{self.name} has been removed from the square class")




sq = Square("MySquare", 5) 

print(sq.removeShape())


#types of inheritance:

#1. single inheritance: when a child class inherits from a single parent class.

class A: 
    pass 

class B(A): 
    pass 

#2. multiple inheritance: when a child class inherits from multiple parent classes.
class P2:
    def method1(self):
        print("Method 2 from Parent 2")
class P1: 
    def method1(self):
        print("Method 1 from Parent 1")



class C(P2, P1):
    pass

## the crux is, how is it going to decide which method to call if both parent have same method. 
## this was the problem in JAVA where we use interfaces, we dont provide implementation at all.
## that is different here tho, here we will understand now. 

c = C()
c.method1()

## which method is going to be called, depends upon how we have inherited the classes.
## so in this case, method1 from P2 is going to be called because we have inherited P2 first and then P1.
## that is called Method Resolution Order (MRO) in python.

##Method overloading vs Method overriding:

##method overriding is already covered in inheritance, where we have a method 
## in the parent class and similar methid in the child class.. same name and parameters.

## Method overloading is when in the same class we have multiple methods with the same signature.
## However, python does not support method overloading, but we can achieve it using default parameters.

# class MethodOverloading:
#     def add(self, a, b):
#         return a + b

#     def add (self, a,b,c): 
#         return a + b + c 


# m1 = MethodOverloading()

# m1.add(1,2) ## this will give an error because we have defined the second add method 
## so first method is completely ignored.


## the workraound is use default parameters or *args. 


class MethodOverloading:
    def add(self, a, b):
        return a + b

    def add(self, a,b,c=0): 
        return a + b + c


m1 = MethodOverloading()

m1.add(1,2) ## this will work now because we have defined the third add method with default parameter.
m1.add(1,2,3) ## this will work now because we have defined the third add method with defa1.add(1,2,3,4) ## this will work now because we have defined the second add method with *args.
