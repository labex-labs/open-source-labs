def print_evenly_indexed_characters():
    s = "H1e2l3l4o5w6o7r8l9d"
    s = [s[i] for i in range(len(s)) if i % 2 == 0]
    print("".join(s))


print_evenly_indexed_characters()
