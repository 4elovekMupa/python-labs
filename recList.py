def rasu(a):
    if a < 0:
        return "ошибка"
    if a < 10:
        return a
    else:
        return rasu(a // 10) + (a % 10)


print(rasu())



