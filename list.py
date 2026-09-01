l2 = l1 = [1, 2, 3, 4, 5]
l1.append(6)
print(l1)
print(l2)

l1[1] = 20
print(l1)

if(20 in l1):
    print("20 is present in the list")

print("Length of the list is: ", len(l1))

dictionary = {"name": "John", "age": 30, "city": "New York"}

for i in dictionary:
    print(i, ":", dictionary[i]) 