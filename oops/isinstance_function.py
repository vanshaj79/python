class Car:
    def __init__(self, usermodel):
        self.__model = usermodel


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "200 HP"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tata")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
