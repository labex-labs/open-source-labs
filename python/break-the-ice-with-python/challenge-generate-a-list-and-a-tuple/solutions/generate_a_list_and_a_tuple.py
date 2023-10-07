def generate_a_list_and_a_tuple():
    lst = input().split(
        ","
    )  # the input is being taken as string and as it is string it has a built in
    # method name split. ',' inside split function does split where it finds any ','
    # and save the input as list in lst variable

    tpl = tuple(lst)  # tuple method converts list to tuple

    print(lst)
    print(tpl)


generate_a_list_and_a_tuple()
