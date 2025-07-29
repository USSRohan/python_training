try:
    a = input("enter the first number :")
    b = input("enter the seocnd number :")
    c = input("enter the third number :")

    if a.isnumeric() == False:
        raise ValueError("A is NOT A NUMBER!")
    
    
    if b.isnumeric() == False:
        raise ValueError("B is NOT A NUMBER")
    
    
    if c.isnumeric() == False:
        raise ValueError("C is NOT A NUMBER")
    
    grate = max(a,b,c)
    print("the gratest number is: ",grate)

except Exception as e:
    print(e)
