# Step 2 Solution


class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print("%s:__get__" % self.name)

    def __set__(self, instance, value):
        print("%s:__set__ %s" % (self.name, value))

    def __delete__(self, instance):
        print("%s:__delete__" % self.name)
