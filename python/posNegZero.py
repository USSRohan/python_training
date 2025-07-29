try:
    a = int(input("Enter a number: "))

    if a>0:
        print("the number is a positive number: ")

    elif a<0:
        print("the number is a Negative number: ")

    else :
        print("the number is 0")

except Exception as e:
    print("U have to enter an number")