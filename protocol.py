##protocols basically means if it walks like a dyck and talks like a duck then it is a duck.
##to exhibit the same behavior as a duck we need to implement the same methods as a duck has.


from typing import Protocol


class Duck(Protocol):
    def quack(self) -> str:
        ...

    def walk(self) -> str:
        ...

class Human: 
    def quack(self) -> str:
        return "Quack!"

    def walk(self) -> str:
        return "Walking like a human."

class Dog: 
    def quack(self) -> str:
        return "Woof!"

    def walk(self) -> str:
        return "Walking like a dog."

def make_it_quack(duck: Duck) -> None: 
    print(duck.quack())
    print(duck.walk())


print(make_it_quack(Human())) ##this will work because Human class implements the same methods as Duck class
print(make_it_quack(Dog())) ##this will work because Dog class implements the same methods as Duck class