dic = {}

string = str(input("Enter a string of data: "))

char = "r"
count = string.count(char)

dic[char]=count

cha = "a"
count = string.count(char)
dic[cha]=count

print(dic)