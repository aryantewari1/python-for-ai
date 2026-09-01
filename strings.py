
print(str.capitalize())
print(str.title())
print(str.upper()) 

l1 = str.split(" ")
print(l1)

str2 = "-".join(l1) 
print(str2)



print(str.replace("hello","hi"))
str3 = '"hello world"'
str4 = "\" hello world \" " ##escape character is used to escape the special characters in python.
print(str3)
print(str4)


lang = "hello in python"

print("hello" in lang)  ## this will return True if hello is present in lang else it will return False.
arr = lang.split(" ")
print(arr)

print("-".join(arr))  ## this will join the array with - in between each element.


##raw strings: you want to give path so it contains backslash so you can use raw strings.
##because normally backslash is used to escape the special characters in python

raw_string = r"C:\Users\aryantewari\Desktop\Python\python-for-ai"
print(raw_string)  ## this will print the raw string as it is without escaping the special