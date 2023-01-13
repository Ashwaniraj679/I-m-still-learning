class Room:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length
        
    def area(self):
        return self.length * self.width

class House:
    def __init__(self, address, *rooms):
        self.address = address
        self.rooms = rooms

    def total_area(self):
        total = 0
        for room in self.rooms:
            total += room.area()
        return total

class BedRoom(Room):
    def __init__(self, name, width, length, bed_count):
        super().__init__(name, width, length)
        self.bed_count = bed_count
        
    def area(self):
        return self.width*self.length

class BathRoom(Room):
    def __init__(self, name, width, length, has_shower):
        super().__init__(name, width, length)
        self.has_shower = has_shower
        
    def area(self):
        return self.width*self.length

# Create room objects
bed1 = BedRoom("Master Bed", 12, 10, 1)
bed2 = BedRoom("Guest Bed", 10, 8, 2)
bath1 = BathRoom("Master Bath", 8, 6, True)
bath2 = BathRoom("Guest Bath", 6, 5, False)

# Create a house object and add the rooms to it
my_house = House("123 Main St", bed1, bed2, bath1, bath2)

# Calculate the total area of the rooms in the house
area = my_house.total_area()
print(f"Total area of the rooms is {area} sq ft")
