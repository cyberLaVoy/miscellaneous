#code writen by LaVoy

#ensures ability to use these functions
from math import pi
from math import sin
from math import cos
from math import tan
from math import e
from math import sqrt

def main():

#this will prompt the user to enter in values
    initialvalues = input("Have an initial point on the graph? If so, enter 'yes'(if not leave blank): ")
    if initialvalues == "yes":
        a = float(input("enter an x point: "))
        b = float(input("enter corrisponding y point: "))
    xvalues = [float(i) for i in input("enter x values, seperated by spaces: ").split()]

#this will create a list of y values, or ask for y values
    yvalues = [ ]
    def create_y():
        for i in range(len(xvalues)):
            x = xvalues[i]
            yvalues.append(eval(equation)) #will adjust to previously entered equation
        print ("x values = " + str(xvalues))
        print ("y values = " + str(yvalues))
        
    stoporgo = input("Need y values calculated? if so, enter 'yes'(if not leave blank): ")
    if stoporgo == "yes":
#this allows the user to change the equation, as desired
        equation = input("Enter the equation needed to solve for y values: f(x) = ")
        create_y()
    else:
        yvalues = [float(i) for i in input("enter y values, seperated by spaces: ").split()]
        
#this will solve for the slope, if desired
    def slope():                      
        for i in range(len(xvalues)):
            print ((b-yvalues[i])/(a-xvalues[i]))
    torunornot = input("Find the slope between initial point and all other points determined? if so, enter 'yes': ")
    if torunornot == "yes":
        slope()
        
#this will allow the user to run program as many times as desired
    mainrun = input("To run this program again, enter 'again': ")
    if mainrun == "again":
        main()
        
#to start program automatically
main()
