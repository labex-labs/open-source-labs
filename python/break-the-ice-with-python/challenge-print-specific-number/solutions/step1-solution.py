def print_specific_number(start = 2000, end = 3201):
    l=[]
    for i in range(start, end):
        if (i%7==0) and (i%5!=0):
            l.append(str(i))
    return (','.join(l))