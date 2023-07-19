import string


def counting_characters_in_strings():
    s = input()
    for letter in string.ascii_lowercase:
        cnt = s.count(letter)
        if cnt > 0:
            print("{},{}".format(letter, cnt))


counting_characters_in_strings()
