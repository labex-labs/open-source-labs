class American():
    @staticmethod
    def printNationality():
        print("I am American")


american = American()
# this will not run if @staticmethod does not decorates the function.
american.printNationality()
# Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
# does not decorate printNationality()
