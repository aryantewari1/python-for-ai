##exactly like javascript, no worries at all. 
##you need to just understand a few things and we are good to go.. 


#1. map - accepts a callback and does something to it.

my_str = "python" 

mapped_str = map(lambda x: x+" ", my_str)
print("".join(mapped_str))

##IMPORTANT- map returns you a lazy iterator object 
## so unliike javascript its not processing fully unless you trigger to process
## so we are forced to use list(), sum(), join() functions to essentially get the output of map

nums = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, nums)
print(list(squared))  # [1, 4, 9, 16, 25] ## here we used list() 

#2 - Filter
## Filter-keeps only the truthy values and remaining goes for nothing..

print(list(map(lambda x: x in ('p' , 't'), my_str)))

mixed = [[], 0, "" , "hello", 12123213  , [[],[[]]]]
##IF YOU PASS NONE TO FILTER IT WILL RETURN U BACK ALL THE TRUTHY VALUES REMOVING FALSY .
print(list(filter(None, mixed)))

#3 Reduce 
## The idea of reduce is to basically accumulate an iterable into a single value.
## the function being passed to reduce accepts three arguments, acc, x, initial value

from functools import reduce
nums = range(0,10)

print(int(reduce(lambda acc,x: acc+x,nums,0)))