#101Computing.net/projection-motion-formula
import math
from processing import *

X = 30
Y = 30
gravity=9.81
angle=70
velocity=80
vx=velocity * math.cos(math.radians(angle))
vy=velocity * math.sin(math.radians(angle))
t=0

def setup():
    strokeWeight(10)
    frameRate(100)
    size(400,400)

def throwBall():
    global X, Y, radius, gravity, t,vx,vy
    background(100)
    fill(0,121,184)
    stroke(255)
    fc = environment.frameCount
    t +=0.02
    X = vx*t
    Y = 400 -(vy*t - (gravity/2)*t*t)

    ellipse(X,Y,30,30)


draw = throwBall 
run()

"""x=x+v*t*cos(a)
y=y+v*t*sin(a)-(1/2)*(g*t)**2

projectile-motion-formula:
x,y represent the starting position. (e.g. position of the tank on the screen),
v velocity represents the initial velocity, in other words the initial power/speed that was used to shoot/throw the projectile,
a angle represents the angle of projection. (At what angle was the projectile thrown)
t timethe time in seconds since the object was thrown. (Starts at 0). The number of frames since the object has been thrown can be used as a frame based game display a frame every x milliseconds.)
g gravity represents the gravity. (On planet Earth: g = 9.81)"""
