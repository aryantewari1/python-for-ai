##Itertools

#1. chain 
## chain takes in multiple iterators and combines into one iterator. 

from itertools import chain
my_list = [1,2,3] 
my_str = "python"
dict={"hello":1, "bye":2}

print(list(chain(my_list,my_str,dict)))

for x in chain(my_list,my_str, dict):
    print(x)

##2 Permutation and combination 

from itertools import permutations, combinations 
## permutations(iterable, number of items at a time)
## combinations(iterable, number of items at a time)
list_1 = [1,2,3]
print(list(permutations(list_1))) ## [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(combinations(list_1,2)))

##3 count has a start, has a step but it goes on forever. 
from itertools import count

for i in count(10, 2):   # start=10, step=2
    print(i)
    if i > 16:
        break
# 10 12 14 16 18

## 4 cycle
## cycle keeps on looping the iterable as a cycle. so once it reaches the end 
## it becomes the start.
from itertools import cycle

colors = cycle(['red', 'green', 'blue'])
for _ in range(7):
    print(next(colors), end=' ')
# red green blue red green blue red
