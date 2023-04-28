def capitalize(s, lower_rest=False):
    return "".join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
