def check(x):
    cnt = 6 <= len(x) and len(x) <= 12
    for i in x:
        if i.isupper():
            cnt += 1
            break
    for i in x:
        if i.islower():
            cnt += 1
            break
    for i in x:
        if i.isnumeric():
            cnt += 1
            break
    for i in x:
        if i == "@" or i == "#" or i == "$":
            cnt += 1
            break
    # counting if total 5 all conditions are fulfilled then returns True
    return cnt == 5


s = input().split(",")
# Filter function pick the words from s, those returns True by check() function
lst = filter(check, s)
print(",".join(lst))
