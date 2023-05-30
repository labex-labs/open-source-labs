def calculate_the_formula_value():
    a = input()
    # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
    total = int(a) + int(2 * a) + int(3 * a) + int(4 * a)
    print(total)


calculate_the_formula_value()
