class Vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(Vehicle):
    pass

School_bus=bus("School,Volvo",180,12)
print("Vehice Name:",School_bus.name,"speed:",School_bus.max_speed,"mileage",School_bus.mileage)
