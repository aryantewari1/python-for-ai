##file i:o means working with files using python. 
##generally we have multiple things we do with the file correct? 
##so in same way we have multiple modes in python to handle file operations
##for example: r,w,a,r+,w+,a+,rb,wb 


# #mode1: r -> read mode: for this mode you need to have the file to exist.
# with open("greetings.txt", "r", newline='', encoding='utf-8') as f: 
#     print(f.read()) ## this will read the entire file and print it on the console.
#     print(f.readline()) ## this will read the first line of the file and
#     print(f.readlines()) ##this will read all the lines and make an array out of it

#     #  best way to read any file avoiding any storage issues is by using for loop to read each line. 
#     for line in f:
#        print(line) ## this will print each line of the file one by one.

#mode2 -> "w" this is the write mode and if file doesnt exist it will create a new file and 
#if the file already exists it will overwrite the existing file.

with open("python1.txt", "w", encoding='utf-8') as f:
    lines=["Hello World2\n", "This is a test file\n", "Python is great!\n"]
    f.writelines(lines) ## this will write the entire list of lines to the file
    f.write("this is the last line of the file\n") ## this will write a single line to the file


# with open("python1.txt", "r", encoding='utf-8') as f:
#     print(f.read())

# #mode3 -> "a" this is the append mode and if file doesnt exist it will create a new file and
# with open("python1.txt", "a", encoding='utf-8') as f:
#     f.write("this will append at the last of the file without overwriting anything") 


# with open("python1.txt", "r", encoding='utf-8') as f:
#     print(f.read())

with open("python1.txt", "r+", encoding='utf-8') as f:
    f.seek(0,2)
    f.write("this will append at the last of the file without overwriting anything\n")
    f.write("helloooeoeoeoeoe") 
    f.seek(0) ## this will move the cursor to the start of the file
    print(f.read())
    

