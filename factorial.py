def rec(a):
    if a == 0:
        return 1
    print(a)
    return rec(a-1) * a


print(rec(7))
