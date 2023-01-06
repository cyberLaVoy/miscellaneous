from math import *

def newtonsmethod():
    x = float(input("x1 = "))
    repeat = int(input("How many times?: "))
    func = input("f(x) = ")
    fund = input("f'(x) = ")
    for i in range(repeat):
        answer = (x - ((eval(func))/(eval(fund))))
        print(answer)
        x = answer

def main():
    newtonsmethod()
main()
