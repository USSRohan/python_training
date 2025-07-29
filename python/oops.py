#class declaration
class person:
    def print_name(self,name):
        print("My name is "+name)

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b

p = person()
p.print_name("rohan")

result = p.add(3,5)
print(result)
result = p.sub(3,5)
print(result)
result = p.mul(3,5)
print(result)