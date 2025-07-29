


try:
    mode = (input("add(1) sub(2) mul(3) div(4)"))
    a = (input("enter the 1st value: "))
    b = (input("enter the 2nd value: "))
    c = (input("enter the 3rd value: "))

    if mode > 4:
        raise ValueError("NOT A VALID INPUT")

    if a.isnumeric() == False:
        raise ValueError("1st value is NOT A NUMBER!")
    
    
    if b.isnumeric() == False:
        raise ValueError("2nd value is NOT A NUMBER")
    
    
    if c.isnumeric() == False:
        raise ValueError("3rd value is NOT A NUMBER")


    if mode == 1:
        y=a+b+c
        print("addition :",y)
    elif mode == 2:
        y = a-b-c
        print("subtraction :",y)
    elif mode == 3:
        y = a*b*c
        print("Multiplication :",y)
    elif mode == 4:
        y=a/b/c
        print(y)
    else:
        raise ValueError("NOT A VALID INPUT")

except Exception as e:
    print(e)