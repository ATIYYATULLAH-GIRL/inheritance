class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
   pass
School_Bus=Bus("Volvo",180, 120)
print("Vehicle name:", School_Bus.name, "Vehicle speed:", School_Bus.max_speed, "Vehicle mileage:", School_Bus.mileage)