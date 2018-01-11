

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
length = 25
n = 100

def square(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)

square(bob, 100, n)

wait_for_user()
