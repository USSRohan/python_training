dis = {}

string = input("enter your string here: ")
c = int

for c in string:
    if not c in dis:
        dis[c] = 0
    else:
        dis[c]+=1

print(dis)