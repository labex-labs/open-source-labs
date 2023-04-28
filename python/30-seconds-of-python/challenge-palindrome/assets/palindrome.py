from re import sub

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
    pass