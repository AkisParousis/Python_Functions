def square_digits(num):
    res = [int(x) for x in str(num)]
    res = [x**2 for x in res]
    res = [str(x) for x in res]
    res = int("".join(res))
    return res
    pass
