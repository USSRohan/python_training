
try:
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

#if isinstance(a,float) and isinstance(b,float):
#if a.isnumeric() and b.isnumeric():

    if a.isnumeric() == False:
        raise ValueError("A is not a number")

    if b.isnumeric() == False:
        raise ValueError("B is not a number")

    
    y= int(a)+int(b)
    print("sum:",y)

except Exception as e:
    print(e)
    print("ENTER A NUMBER")

