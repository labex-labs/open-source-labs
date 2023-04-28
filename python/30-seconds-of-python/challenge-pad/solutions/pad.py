from math import floor


def pad(s, length, char=" "):
    return s.rjust(floor((len(s) + length) / 2), char).ljust(length, char)
