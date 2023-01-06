from math import *


def grabvalues():
    xvalues = []
    dur = int(input("How many x values? "))
    for i in range(dur):
        possible = eval(input("x value #" + str(i+1) + ": "))
        xvalues.append(possible)
    return xvalues


def grabfunction(xvalues):
    answers = []
    function = input("f(x) = ")
    for i in range(len(xvalues)):
        x = xvalues[i]
        answers.append(eval(function))
    return answers

    
def results(xvalues, answers):
    for i in range(len(xvalues)):
        print("f(" + str(xvalues[i]) + ") = " + str(answers[i]))
    add = input("Would you like these values all together? (y or n): ")
    if add == "y":
        total = 0
        for i in range(len(answers)):
            total += answers[i]
        print(total)
            


def main():
    xvalues = grabvalues()
    answers = grabfunction(xvalues)
    results(xvalues, answers)
main()
