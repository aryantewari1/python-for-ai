##polymorphism is basically when you are calling something, it will always depend upon
##the context you are calling it from.

class Animal(): 
    x =6
    def __init__(self, breed): 
        self.breed = breed

    def speak(self): 
        print(f"{self.breed} makes a sound")

class Dog(Animal): 
    def __init__(self, breed, name):
        super().__init__(breed)
        self.name = name

    def speak(self):
        print(f"{self.name} barks")


for animal in [Animal("Dog"), Dog("Dog", "Rex")]:
    animal.speak()
##the idea is that the same method name can be used for different types of objects,
# and the correct method will be called based on the object type. 
# This is known as polymorphism.

##polymorphism can also be achieved through operator overloading, 
# where the same operator can have different meanings based on the context. 
# For example, the "+" operator can be used to add numbers, concatenate strings, or combine lists


class Integer(): 
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value



i1 = Integer(5)
i2 = Integer(10)

print(i1 + i2)  ## so when u do + the _add_ method is called and it returns the sum of the two values.
print(i1)
    