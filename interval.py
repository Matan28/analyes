import math


def find_root(f, a, b, eps=0.000001):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    c = (a + b) / 2
    if f(a) * f(b) > 0:
        return None
    counter = 0
    while abs(f(c)) > eps:
        if f(a) * f(c) < 0:
            b = c
            counter += 1
        else:
            a = c
            counter += 1
        c = (a + b) / 2
    print(counter)
    return c


def bisection(f, xl, xr, eps=0.00001):
    '''
    This code made by Matan Tal. what it does is every iteration we divided the border and
    update the borders.
    :param f: the function
    :param xr: x value for the right border
    :param xl: x value for left border
    :param eps: the tolerance gow many iterations
    :return: the root
    '''
    xm = 0
    counter = 0
    while (xr - xl) > eps:
        xm = (xr + xl) / 2
        if f(xl) * f(xm) > 0:
            xl = xm
            counter += 1
        else:
            counter += 1
            xr = xm
    print('iteration number: ', counter)
    return xm


def secant(f, x0, x1, tolerance=0.00001, NMAX=100):
    '''
    using the secant method we get the root from the equation
    :param f: function
    :param x0: start values
    :param x1: start values
    :param tolerance: tolerance value(optional)
    :param NMAX: max number of iterations(optional)
    :return: root of the equation
    '''
    n = 1
    counter = 0
    while n <= NMAX:
        x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        n += 1
        if abs(x2 - x1) < tolerance:
            print('Iteration number: ', counter)
            return x2
        else:
            x0 = x1
            x1 = x2
            counter += 1
    return False


def newtonraphson(func, derivativ_func, initial_value, tolerance=0.00001, NMAX=100):
    '''
    Newton Raphson method to find roots
    :param func: function that given
    :param derivativ_func: derivative of the function
    :param initial_value: initial value
    :param tolerance: value(optional)
    :param NMAX: max number of iterations(optional)
    :return: root of the equation
    '''
    n = 1
    counter = 0
    while n <= NMAX:
        x1 = initial_value - (func(initial_value) / derivativ_func(initial_value))
        n += 1
        if abs(x1 - initial_value) < tolerance:
            print('iteration number: ', counter)
            return x1
        else:
            counter += 1
            initial_value = x1
    return False


def intervals_creator(left_border, right_border, interval_jump=0.5):
    borders = []
    update_border = left_border
    border_amount = round((right_border - left_border) / interval_jump)
    for i in range(border_amount):
        temp = [update_border, update_border + interval_jump]
        borders.append(temp)
        update_border += interval_jump
    return borders


if __name__ == '__main__':
    # print('The root from bisection is: ',find_root(lambda x: 16 * x ** 3 - 16 * x ** 2 + 1, 100, -100))
    interval_border = intervals_creator(-10, 10)
    print('\n\nbisection method:')
    for i in interval_border:
        print('border:[', i[0], i[1], ']',bisection(lambda x: 16 * x ** 3 - 16 * x ** 2 + 1, i[0], i[1]))

    for i in interval_border:
        print('border:[', i[0], i[1], ']',bisection(lambda x: 48 * x ** 2 - 32 * x, i[0], i[1]))

    for i in interval_border:
        print('border:[', i[0], i[1], ']',bisection(lambda x: 96 * x - 32, i[0], i[1]))

    print('\n\n\n\n\n\n\n\nsecant method:')
    for i in interval_border:
        print('border:[', i[0], i[1], ']', secant(lambda x: 16 * x ** 3 - 16 * x ** 2 + 1, i[0], i[1]))

    for i in interval_border:
        print('border:[', i[0], i[1], ']',secant(lambda x: 48 * x ** 2 - 32 * x, i[0], i[1]))

    for i in interval_border:
        print('border:[', i[0], i[1], ']',secant(lambda x: 96 * x - 32, i[0], i[1]))

    print('\n\nNewton Raphson method:')
    print('The root using Newton Raphson,\nFrom function:\n16x^3-16x^2+1:\n'
          'function Derivative:\n48x^2-32x: The root:',
          newtonraphson(lambda x: 16 * x ** 3 - 16 * x ** 2 + 1,
                        lambda x: 48 * x ** 2 - 32 * x, 2))
    print('The root using Newton Raphson,\nFrom function:\n48x^2-32x:\n'
          'function Derivative second time:\n96x-32: The root:',
          newtonraphson(lambda x: 48 * x ** 2 - 32 * x,
                        lambda x: 96 * x - 32, 7))

    print('Q5:bisection:')
    for i in interval_border:
        print(bisection(lambda x: x * math.e ** -x - 0.25, i[0], i[1]))
    print('Q5:secant:')
    for i in interval_border:
        print(secant(lambda x: x * math.e ** -x - 0.25, i[0], i[1]))
    for i in range(1, 5):
        print('The root using Newton Raphson,\nFrom function:\n16x^3-16x^2+1:\n'
              'function Derivative:\n48x^2-32x: The root:',
              newtonraphson(lambda x: 16 * x ** 3 - 16 * x ** 2 + 1,
                            lambda x: 48 * x ** 2 - 32 * x, i))
# code
