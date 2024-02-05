class Car:
    __speed = 0

    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    # getter
    @property
    def speed(self):
        return self.__speed

    # setter
    @speed.setter
    def speed(self, value):
        if (value < 0):
            raise ValueError("speed must be positive!")
        self.__speed = value


car = Car("Purch", 4)
# print(car.__name)
car.speed = -5
# print(car.read_only_name)
