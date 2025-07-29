
class city:
    def cityDetails(self,name,country):
        self.name = name
        self.country = country

    def printCityDetails(self):
        print("city name: "+self.name)
        print("Country name: "+self.country)

p1 = city()
p1.cityDetails("delhi","india")

p1.printCityDetails()

p2 = city()
p2.cityDetails("london","UK")

p2.printCityDetails()
