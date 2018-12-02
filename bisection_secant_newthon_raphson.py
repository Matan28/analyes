"""
Bisection, Secant & Newton Raphson Method.
"""

import math

"""
* Variable Description:
*
* f			:	Given function
* f_		:	Derivative of f
* [a, b]	:	End point values
* NMAX		:	Max number of iteration==s
"""


def bisection(f, a, b, tolerance=0.001, NMAX=100):
    """
    Takes a function f, start values [a,b], tolerance value(optional) TOL and
    max number of iterations(optional) NMAX and returns the root of the equation
    using the bisection method.
    not good for double
    """
    n = 1

    while n <= NMAX:
        c = (a + b) / 2.0
        print("iter=%s\ta=%s\tb=%s\tc=%s\tf(c)=%s" % (n, a, b, c, f(c)))
        n += 1
        if f(c) == 0 or (b - a) / 2.0 < tolerance:
            return c
        else:
            n = n + 1
            if f(c) * f(a) > 0:
                a = c
            else:
                b = c
    return False


def secant(f, x0, x1, tolerance=0.001, NMAX=100):
    """
    Takes a function f, start values [x0,x1], tolerance value(optional) TOL and
    max number of iterations(optional) NMAX and returns the root of the equation
    using the secant method.
    """
    n = 1
    while n <= NMAX:
        x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        n += 1
        if abs(x2 - x1) < tolerance:
            return x2
        else:
            x0 = x1
            x1 = x2
    return False


def newtonraphson(f, f_, x0, tolerance=0.001, NMAX=100):
    """
    Takes a function f, its derivative f_, initial value x0, tolerance value(optional) TOL and
    max number of iterations(optional) NMAX and returns the root of the equation
    using the newton-raphson method.
    """
    n = 1
    while n <= NMAX:
        x1 = x0 - (f(x0) / f_(x0))
        n += 1
        if abs(x1 - x0) < tolerance:
            return x1
        else:
            x0 = x1
    return False


# if __name__ == '__main__':


# Invoking Bisection Method
print('Invoking Bisection Method')
print(bisection(lambda x: x ** 3 - x - 2, 1, 2))

# Invoking Secant Method
print('Invoking Secant Method')
print(secant(lambda x: x ** 3 - x - 2, 30, 10))

# Invoking Newton Raphson Method
print('Invoking Newton Raphson Method')
print(newtonraphson(lambda x: x ** 3 - x - 2, lambda x: 3 * x ** 2 - 1,
                    -144.1131))
