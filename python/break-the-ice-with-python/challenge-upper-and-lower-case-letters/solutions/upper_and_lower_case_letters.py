def upper_and_lower_case_letters():
    word = input()
    # sum function cumulatively sum up 1's if the condition is True
    upper = sum(1 for i in word if i.isupper())
    lower = sum(1 for i in word if i.islower())

    print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


upper_and_lower_case_letters()
