print("<<<<<<<<""WITH USING TEMP VARIABLE"">>>>>>>>")

a =int(input("Enter the value of a :"))
b =int(input("Enter the value of b :"))
temp = None

temo = a
a = b
b = temp

print("After the Swapping value of a :",a)
print("After the Swapping value of b :",b)

print("<<<<<<<<<WITHOUT USING TEMP VARIABLE"">>>>>>>>")

a =int(input("Enter the value of a :"))
b =int(input("Enter the value of b :"))

a,b = b,a

print("After the Swapping value of a :",a)
print("After the Swapping value of b :",b)