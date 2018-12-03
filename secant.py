from sympy import *
import cmath
import math
import numpy as np


def func(symbolic_function):
    '''

    :param symbolic_function: symbolic expresion
    :return: magmatic expresion
    '''
    return lambdify(x, symbolic_function, 'numpy')


def find_roots(rangex):
    intervals = []
    j = rangex[0]
    for _ in range((abs(rangex[1]) + abs(rangex[0])) * 2):
        intervals.append([j, j + 0.2])
        j = j + 0.2
    return intervals


def intervals_f(Start_Domain, End_Domain, interval_jump):
    domains = []
    parameter = Start_Domain

    tmp = (End_Domain - Start_Domain) / interval_jump
    for i in range(int(tmp)):
        domains.append(parameter)
        parameter += interval_jump

    domains.append(End_Domain)
    return domains


def secant(rangex, fx, x0, x1, eps, itration):
    while abs(x1 - x0) > eps or itration == 0:
        # if(isinstance(fx(x0),complex) == True or isinstance(fx(x1),complex) == True):
        # return None
        if fx(x1) - fx(x0) < eps:
            return None
        x = x1 - fx(x1) * ((x1 - x0) / (fx(x1) - fx(x0)))
        x0 = x1
        x1 = x
        itration -= 1
    return x


def all_roots(fx, eps, rangex, itration):
    roots = []
    k = 0
    almostE = 0.01
    intervals = intervals_f(rangex[0], rangex[1], 0.5)
    for i in intervals:
        x0 = (2 * i + 0.1) / 3
        x1 = (2 * i + 0.1) / 2
        temp = secant(rangex, fx, x0, x1, eps, itration)

        if temp != None:
            if (len(roots) == 0):
                if temp >= rangex[0] and temp <= rangex[1]:
                    roots.append(temp)
            else:
                if temp >= roots[k] - almostE and roots[k] + almostE >= temp:
                    continue
                if temp <= rangex[1] and temp >= rangex[0]:
                    roots.append(temp)
                    k = k + 1
    if len(roots) == 0:
        return None
    return roots


if __name__ == '__main__':
    x = Symbol('x')
    # gx = ln(x*2-2*x)+cos(x3-1)+exp(2(x**2)-3*x+4)
    gx = cos(x ** 3 - 1)
    fx = func(gx)

    print(all_roots(fx, 0.0001, [0, 3], 100))
# code
