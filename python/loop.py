number = int(input("enter an number: "))

i = int(1)
while i <= number:
    
    if i % 2 == 0:
        #print(i,end=" :the number is even \n ")
        print(f"the number is even {i}")

    else:
        #print(i,end=' :number is odd ')
        print(f"the number is odd {i}")

    i += 1
    
