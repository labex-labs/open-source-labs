from re import sub


def camel(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return "".join([s[0].lower(), s[1:]])
