from re import sub

def camel(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    pass