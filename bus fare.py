class Bus:
    def __init__(self, passengers, fare_per_passenger): 
        self.passengers,self.fare = passengers, fare_per_passenger
class TotalFare(Bus):
    def calculate(self): 
        return self.passengers * self.fare
bus = TotalFare(42, 150); print("Total Fare:", bus.calculate())