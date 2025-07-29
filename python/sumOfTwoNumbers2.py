#try:
a = input("Enter the first number: ")

b = input("Enter the second number: ")

#if isinstance(a,float) and isinstance(b,float):
#if a.isnumeric() and b.isnumeric():

if a.isnumeric() == False:
    print("A is not a number")

if b.isnumeric() == False:
    print("B is not a number")

else:
    y= a+b
    print(y)
