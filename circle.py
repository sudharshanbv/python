from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1
n = 20
radius = 10
circumference = 2*3.14*radius
length = circumference / n

def circle(t, length, n, radius):
    pu(t)
    fd(t, length)
    lt(t)
    pd(t)
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)

circle(bob, 100, n, radius)

wait_for_user()
