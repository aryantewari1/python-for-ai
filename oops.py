class Animal : 
    eyes=True ## class level attribute
    def __init__(self, breed, legs, hands): ##constructor defined using init method
        self.breed = breed
        self.legs = legs  ## instance variable defined using self keyword
        self.hands = hands
        self.value = 10 ## instance variable defined using self keyword

    
    def sound(self):  ##instance method defined using self keyword
        print(f"{self.breed} makes sound")

    @classmethod 
    def has_eyes(cls): ## class method defined using cls keyword
        print(f"All animals have eyes: {cls.eyes}")

    @staticmethod 
    def is_breathe_oxygen(): ## static method defined without self or cls keyword
        print("All animals breathe oxygen")


dog = Animal("Dog", 4, 0)
print(dog.breed)
dog.sound()
Animal.has_eyes()
Animal.is_breathe_oxygen()
print(Animal.eyes) 

##child class in case of inheritance
class Dog(Animal): ## Dog class inherits from Animal class  
    def __init__(self, breed,legs,hands, naam): 
        super().__init__(breed,legs,hands) 
        self.naam = naam
        self.value=20

    def sound(self): ## overriding the sound method of Animal class
        print(f"{self.naam} barks")

    def __str__(self): ## overriding the __str__ method of Animal class
        return f"{self.naam} is a {self.breed} with {self.legs} legs and {self.hands} hands"


d1 = Dog("Dog",4,0, "Tommy")
print(d1.naam)
d1.sound()

##Dunder/magic methods in python are special methods that start and end with double underscores
## __init__ is a dunder method that is called when an object is created.
##similarly we have other dunder methods like __str__, __repr__, __add__, __sub__ , __eq__, __len__ etc

print(d1) ## this will print the memory address of the object <__main__.Animal object at 0x100f0cd70>
##but if we define the __str__ method in the class then it will print the string representation of the object


##Encapsulation in python is implemented using protected variables, getters, setters and deleters
##the hidden concept is however descriptors which we will understand later. 


class Bank: 
    def __init__ (self, balance): 
        self._balance = balance 
        """
        using underscore tells developer that this partcular shud not be exposed
        anywhere in the code as it is protected.
        but python itself doesnt protect it you can still access normally so that is setting up the
        intent for developers

        """

    ##getters 
    @property
    def balance(self): 
        """
        it is a convention to use the same name as the variable inside 
        the getter, setter and deleter functions
        """
        return self._balance 
    
    @balance.setter
    def balance(self,val):
        self._balance  = val




b1 = Bank(1000) 
b1.balance=100000
print(b1.__dict__)
print(b1._balance) ## this will print the balance of the bank account

##Generally just like in normal objects you can add as many variables as you want to an object 
##So basically what i mean is

b1.y = 5; ##y gets added to the __dict__ of that b1 object 

##However there is a way you can control this and it is by defining slots 
## __slots__ = ('x','y') means the class will have these two varaibles only 
## __slots__ removes the dict object so it removes the scope of adding new variables in the first place.

class Point: 
    __slots__ = ('x','y')
    def __init__ (self,x,y):
        self.x = x
        self.y =y 

p =Point(2,3) 

p.z =5
print(p.z) ##error-> 'Point' object has no attribute 'z' and no __dict__ for setting new attributes
print(p.x) 