class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand # making variable private by giving __ before the variable name
        self.model = usermodel
        
    def get_brand(self):
        return self.__brand + "!"

    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fullname(self):
        return f"{super().fullname()} ({self.battery_size})"
    
    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
safari = Car("Tata", "safari")

print(my_tesla.model)
# print(my_tesla.__brand) # you cannot access the peivate variables 
print(my_tesla.get_brand())
print(my_tesla.fullname())
print(my_tesla.fuel_type())

print(safari.fuel_type())
