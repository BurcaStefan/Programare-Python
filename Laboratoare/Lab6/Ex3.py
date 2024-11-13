class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"Kilometrajul mașinii este de {self.mileage} km pe galon."

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"Kilometrajul motocicletei este de {self.mileage} km per galon."

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"Capacitatea de remorcare este de {self.towing_capacity} kg."




car = Car("Ford", "Focus", 2012, 30)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, 55)
truck = Truck("Ford", "F-150", 2018, 13000)

print(car.get_info())
print(car.calculate_mileage())

print(motorcycle.get_info())
print(motorcycle.calculate_mileage())

print(truck.get_info())
print(truck.calculate_towing_capacity())