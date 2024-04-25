# Write a Python program to count the number of lines in a text file

path = ""C:\\Users\\LENOVO\\Desktop\\python23\\python23\\Assigment\\Module – 4 (Advance python programming)\\file.txt"
f=open(path,'r')

s=f.readlines()

count=len(s)

print(f"The number of lines in the file is : {count}")