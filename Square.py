'''функция которая передает три аргумента- коэффиценты квадртного уравнения.
функция должна решать полученное квадратное уравнение и возвращать результат'''


def kvadratnoe (a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "НЕТ КОРНЕЙ"
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)


print(kvadratnoe(2, 3, -4))