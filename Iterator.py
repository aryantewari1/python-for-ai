# ##any class that basically provides you object that can be looped over is an iterator. 

# ##for example
# my_list = [1, 2, 3, 4, 5]; 

# list_iterator = iter(my_list);
# print(next(list_iterator));
# print(next(list_iterator));

# ##esentially we are using __iter__ and __next__ methods to create an iterator. 
# ##just like we use len() in the behind its actually __len__ method that is being called.

# # lets try to create our own for loop
# ## for loop behind the scenes uses __next__ and __iter__ only. 
 
# for x in my_list: 
#     print(x); 

# #behind the scenes its actually 

# y = iter(my_list); ## create an iterator object from the list  
# while y: 
#     try: 
#         print(next(y)); ## get the next item from the iterator
#     except StopIteration: 
#         break; ## if there are no more items, break the loop



# ##creating our own class

# class Countdown:
#     def __init__(self, value):
#         self.current = value

#     def __iter__(self): 
#         return self

#     def __next__(self):
#         if(self.current<0):
#             raise StopIteration 
#         else: 
#             self.current -= 1
#         return self.current+1

# c = Countdown(4) 

# for x in c: 
#     print(x)


from itertools import chain


list1 = [1,2,3] 
list2 = [4,5,6]
combined = chain(list1,list2)
print(list(combined))
for x in combined:
    print(x)