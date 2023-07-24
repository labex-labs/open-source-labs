def print_the_longest_string(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)


s1, s2 = input().split()
print_the_longest_string(s1, s2)
