'''Написать функцию, принимающая 1 аргумент целое число в десятичной системе счистления,
которая будет переводить это число в двоичную систему счистления.'''
def funkcua (a):
    qwerty=""
    while a//2!=0:
        qwerty += (str(a%2) + " ")
        a//=2
    qwerty += "1"
    c = qwerty.split(" ")
    c.reverse()
    qwerty = "".join(c)
    qwerty = int(qwerty)
    return qwerty
print (funkcua(71))