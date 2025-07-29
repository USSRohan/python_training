from abc import ABC,abstractmethod

class person():
    cityName ="mumbai"
    def printName(self,name):
        print(name)
class person_name(person):
    def printDetails(self):
        print("some message")
class person_name2(person):
    def printMoreDetails(self):
        print("anything")

obj = person_name()
obj.cityName = "new york"
print(obj.cityName)
obj.printName("rehan\n")

obj = person_name2()
obj.cityName = "london"
print(obj.cityName)
obj.printName("gabby")

