##annotation describes the type of different python variables, its a basic thing but yeah
##annotation just provides we will still need static type checker modules to make things happen.

x:int = 5
x = "aryan" ##this is not going to throw any error. ##unless we use, static checker modules like mypy

my_list: list[int | str | bool] = [1, 2, 3, "aryan", True]
print(my_list)

my_tuple: tuple[int, *tuple[str, ...]] = (1, 'aryan', 'hello', 'world')
print(my_tuple) 

my_dict: dict[str, int|str] = {"aryan": 1, "hello": 2}
print(my_dict)  

my_set: set[int | str] = {1, 2, 3, "aryan"}
print(my_set)

def add_numbers(a: int, b: int) -> int:
    return a + b

add_numbers(5, 10) ##this is going to work


##Lets understand different types of annotations 
##this is the old way.. modern python doesnt follow

from typing import Optional, Union, List, Tuple, Dict, Set, TypedDict, Any 

##Optional is used to indicate that a variable can be of a certain type or None
x: Optional[int] = None 
print(x)

y: Union[int, str] = 5
y = "aryan"
y = 5

my_list1: List[int] = [1, 2, 3, 4, 5] 
my_tuple1: Tuple[int, str] = (1, "aryan")
my_dict1: Dict[str, int] = {"aryan": 1, "hello": 2}
my_set1: Set[int] = {1, 2, 3} 

##TypedDict is used to define a dictionary with specific keys and value types

class Book(TypedDict):
    title: str 
    author:str 
    pages:int
    price:int


book : Book = {"title": "Python Programming", "author": "Aryan", "pages": 300, "price": 500}
print(book)

#any is used to indicate that a variable can be of any type
x: Any = 5 #it forces typechecker to avoid checking the type of variable x. 
## it is dangerous and must be used in controlled manner. 


