
def add(a,b):
    return a + b 
def sub(a,b):
    return a - b 
def mul(a,b):
    return a * b 
def div(a,b):
    if b == 0:
        raise ValueError("B cannot be 0!!")
    return a / b


try:
    
    Operation = (input("enter what operation u want to perform add(1) sub(2) mul(3) div(4): "))
    if not Operation.isdigit():
        raise ValueError("the operation value should be in the range of 1-4")
    Operation = int(Operation)
    
    #a = (input("Enter the first number: "))
    #b = (input("Enter the second number: "))

    #if a !=float and b != float:
    #    raise ValueError("Both number are not valid")
    #elif a != float:
    #    raise ValueError("First number is not valid")
    #elif b != float:
    #    raise ValueError("Second number is not valid")
    a_input = input("Enter the first number: ")
    b_input = input("Enter the second number: ")

    try:
        a = float(a_input)
    except ValueError:
        raise ValueError("First number is not valid")

    try:
        b = float(b_input)
    except ValueError:
        raise ValueError("Second number is not valid")
    

    if Operation == 1:
        print("result: ",add(a,b))
    elif Operation == 2:
        print("result: ",sub(a,b))
    elif Operation == 3:
        print("result: ",mul(a,b))
    elif Operation == 4:
        print("result: ",div(a,b))
    else:
        raise ValueError("Not a valid input")
except Exception as e:
    print(e)