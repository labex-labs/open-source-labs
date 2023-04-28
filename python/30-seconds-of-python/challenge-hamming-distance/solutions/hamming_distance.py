def hamming_distance(a, b):
    return bin(a ^ b).count("1")
