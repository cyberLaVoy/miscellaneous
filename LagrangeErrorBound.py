import math
from math import pi, e

def lagrange(M, x, c, n, isLn):
    if isLn:
        M = abs( lnNthDerivative(x, n) )
    value = abs( (M/math.factorial(n+1))*((x-c)**(n+1)) )
    return value

def degree(M, x, c, tollerance, isLn):
    n = 1
    v = lagrange(M, x, c, n, isLn) 
    while True:
        v = lagrange(M, x, c, n, isLn) 
        if v < tollerance:
            return n
        n += 1

def lnNthDerivative(x, n):
    value = (-1)**(n-1) * math.factorial(n-1)/x**n
    return value

def main():
    isLn = False
    M = input("M = ")
    if M == "ln":
        isLn = True
        M = -1
    else:
        M = float(eval(M))
    x = input("x = ")
    x = float(eval(x))
    c = input("c = ")
    c = float(eval(c))
    tollerance = input("tollerance = ")
    tollerance = float(eval(tollerance))
    print( degree(M, x, c, tollerance, isLn) )
main()