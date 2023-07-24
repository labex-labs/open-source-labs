class Person(object):
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


aMale = Male()
aFemale = Female()
print(aMale.getGender())
print(aFemale.getGender())
