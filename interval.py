import math


def find_root(f, a, b, eps=0.0001):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    c = (a + b) / 2
    if f(a) * f(b) > 0:
        return None

    while math.abs(f(c)) > eps:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    return c


def find_root_2(f, xr, xl, eps=0.0001):
    xm = 0
    while (xr - xl) > eps:
        xm = (xr + xl) / 2
        if f(xl) * f(xm) > 0:
            xl = xm
        else:
            xr = xm
    return xm


if __name__ == '__main__':
    print(find_root(lambda x: math.cos(x), 2, -2))
    print(find_root_2(lambda x: math.sin(x) + x ** 2 - 2, 2, -2))
# code
