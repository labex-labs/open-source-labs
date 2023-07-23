class Car:
    name = "Car"

    def __init__(self, name=None):
        self.name = name


honda = Car("Honda")
print("%s name is %s" % (Car.name, honda.name))

toyota = Car()
toyota.name = "Toyota"
print("%s name is %s" % (Car.name, toyota.name))
