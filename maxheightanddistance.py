from math import sin
from math import cos
from math import pi
from math import radians

def maxheight(v, theta):
    for i in range(len(theta)):
        print (((v*sin(theta[i]))**2)/(2*9.8))

def distance(v, theta):
    for i in range(len(theta)):
        print ((2*v**2*cos(theta[i])*sin(theta[i]))/9.8)

def main():
    
    v = float(input("enter magnitude of initial velocity: "))
    theta = [float(eval(i)) for i in input("enter theta values (in radians), seperated by spaces: ").split()]

    maxheight(v, theta)
    distance(v, theta)
    
main()
