num = float(input("enter a number: "))

try:
    if num > 100:
        raise("The number is MORE THAN 100")
    else:
        print("The number is LESS than 100")
except Exception as e:
    print(e)