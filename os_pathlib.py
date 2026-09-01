import os
from pathlib import Path

## lets understand os first 
## so os is basically a module that lets you interact wit the OS. 

## but the purpose we are going to be using it for now is to get the path.

path = os.getcwd()
print(path) 
print(os.path.isfile("python1.txt")) ## this will check if the file exists or not and return True or False
print(os.path.split(path))
print(os.path.abspath("python1.txt")) ## this will give the absolute path of the file

path1 = Path("/Users/aryantewari/Desktop/Python/python-for-ai/python1.txt")

print(path1.name)
print(path1.stem)
print(path1.suffix)
print(path1.parent)
print(path1.absolute())