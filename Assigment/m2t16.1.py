# Write a Python program to count the occurrences of each word in a given sentence.

s=input("enter a string : ")

d={}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)  