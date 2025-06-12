class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel

    @property #it allows to make variables read only and also makes your method a property to access
    def get_model(self):
        return self.__model

    def get_brand(self):
        return self.__brand


my_car = Car("Honda", "City")
# my_car.get_model = "Civic"
print(my_car.get_model)
