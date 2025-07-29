
from datetime import datetime

current_datetime = datetime.now()
#formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
#get input from the user and write it into the file  

name = str(input("enter your name: "))
age = str(input("enter your age: "))

#cars = ["ford","volvo","bmw","merc",'ferrari']

with open("sample.txt",'w') as file:
    file.write(f"name: {name}  age: {age}  {current_datetime}")