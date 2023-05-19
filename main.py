#parent class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
        
#two child classes
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        
    def display_info(self):
        super().display_info()
        print(f"{self.num_doors} doors")
        

class Pickup(Vehicle):
    def __init__(self, make, model, year, bed_size):
        super().__init__(make, model, year)
        self.bed_size = bed_size
        
    def display_info(self):
        super().display_info()
        print(f"{self.bed_size} bed size")

# Prompt user to create vehicles
vehicles = []
while True:
    choice = input("Add a car or pickup truck (c/p)? Press q to quit. ")
    if choice.lower() == "q":
        break
        
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    year = input("Enter the year: ")
    
    if choice.lower() == "c":
        num_doors = input("Enter the number of doors: ")
        vehicle = Car(make, model, year, num_doors)
    elif choice.lower() == "p":
        bed_size = input("Enter the bed size: ")
        vehicle = Pickup(make, model, year, bed_size)
    else:
        print("Invalid choice")
        continue
        
    vehicles.append(vehicle)

# Display vehicle information
for vehicle in vehicles:
    vehicle.display_info()
