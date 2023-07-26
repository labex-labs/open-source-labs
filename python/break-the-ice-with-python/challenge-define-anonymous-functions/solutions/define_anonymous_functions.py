# No different way of code is written as the requirment is specificly mentioned in problem description
def define_anonymous_functions():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
    print(list(squaredNumbers))               # converting the object into list


define_anonymous_functions()
