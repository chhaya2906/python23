# Write a Python program to read a random line from a file

import random

def read_random_line():
    file = open("C:\\Users\\LENOVO\\Documents\\file management\\test.txt","r")
    print(file.readlines())
    
    file.close
    

read_random_line()