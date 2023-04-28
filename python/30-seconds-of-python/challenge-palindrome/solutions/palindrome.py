from re import sub


def palindrome(s):
    s = sub("[\W_]", "", s.lower())
    return s == s[::-1]
