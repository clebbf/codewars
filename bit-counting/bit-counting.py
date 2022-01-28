def count_bits(n):
    return list(map(str, bin(n))).count("1")