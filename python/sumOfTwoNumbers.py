#try:
a = (input("Enter the first number: "))
#except Exception as e:
#    print("please enter the a number")

#try:
b = (input("Enter the second number: "))
#except Exception as a:
#    print("please enter the a number")


if isinstance(a,int) and isinstance(b,int):
#if a.isnumeric() and b.isnumeric():
    y = a+b
    print(y)

else:
    print("a number was not given")

