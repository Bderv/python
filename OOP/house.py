class House:
    def __init__(self, numGarages, dogName):
        self.numLivingRooms = 1
        self.numBaths = 3
        self.numBedrooms = 4
        self.numBackyard = 1
        self.garageCount = numGarages
        self.nameofOwner = dogName
        self.solarPanels = 0
    def addSolarPower(self, amount):
        self.solarPanels += amount
        return self
    def changeDogName(self,newName):
        self.nameofOwner = newName
        return self
    def displayHouse_info():
    print(f"your house has {self.garageCount} garages with a dog named {self.nameofOwner}.You also have {self.solarPanels} solar panels")
    return self

# create instacnes of house clas(house objects)
house1 = House(2, "Junior")
house2 = House(0, "Jeff")
house3 = House(1, "Rover")
house4 = House(0, "Beamer")

# print(house1.solarPanels)
# print(house2.solarPanels)
# print(house3.solarPanels)
# print(house4.solarPanels)

# house1.garageCount = 4
house1.addSolarPower(3).addSolarPower(5).changeDogName("poopface")
house2.addSolarPower(2)
# print(house1.garageCount)
print(house1.solarPanels)
print(house2.solarPanels)
#the value of a function call is whatever it returns.
print(house1.nameOfOwner)
print(house2.nameOfOwner)
print(house3.nameOfOwner)
print(house4.nameOfOwner)
