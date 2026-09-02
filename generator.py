# ##Generator uses yield 
# ##lets understand by comparison 

# class Countdown:
#     def __init__(self, value): 
#         self.current= value 

#     def __iter__(self): 
#         return self

#     def __next__(self):
#         if(self.current<=0):
#             raise StopIteration
        
#         self.current -=1

#         return self.current


# c1 = Countdown(5)

# for x in c1: 
#     print(x) 

# c2 = Countdown(6) 

# c2_iter = iter(c2) 

# while True: 
#     try:
#         val = next(c2_iter) 
#     except StopIteration:
#         break
#     print(val)

##Generator -> 

def gen_countdown(start): 
    while start>0: 
        yield start
        print(f"{start} is the value here")
        start-=1

c3 = gen_countdown(2)

while True: 
    try:
        val = next(c3)
    except StopIteration: 
        print("stopped")
        break
    print(val)

##Generators are for laziness and memory efficieny. 
## generators mein basically yield jab aata hai toh waha function ruk jaata hai
## uske baad next() call kroge toh hi function start hoga uss point se. 

##Generator expressions 

#LIST COMPREHENSION
# my_list = [x*x for x in range(15)] 
# print(my_list)

# my_generator_list = (x*x for x in range(15)) 

# print(next(my_generator_list))
# print(next(my_generator_list))
# print(next(my_generator_list))
# print(next(my_generator_list))
# print(next(my_generator_list))

##instead of loading up all at once, we do it one a time. 






