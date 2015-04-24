# clockFind.py was a program used to test how
# well the camera worked and if it could see
# the goal - a pink obstacle.

# Author: Michael Arteaga
# Date: April 2015

from Myro import *

def main():
    while True:
        #move slightly while taking pictures
        turnLeft(.3,.1)
        pic = takePicture()
        show(pic) # for our eyes
        if isPink():
            goForward()
            return
        else: 
            # cannot see pink
# isPink() returns true if the obstacle in sight
# is pink        
def isPink():
    pic = takePicture()
    show(pic)
    pixel = getPixel(pic, 128,96)
    red, green, blue = getRGB(pixel)
    if (red > 225 and green < 150):
        #print("PINK!")
        return True
    else: 
        #print("NOTHING")
        return False

# goForward() drives the robot to the goal
# when arriving at the object, program will
# center itself
# Josh       
def goForward():
    while True:
        left, center, right = getObstacle()
        
        forward(-.5)
        
        #robot is centered on an object
        if center > 950:
            if left < 100:
                if right < 100:
                    stop()     
                    beep(2,850)   
                    return         
        if center > 950:
            #robot senses a cup to the left,
            #turn left to center cup
            if left > 400:
                turnLeft(.2,.5)
                stop()
                beep(2,850)
                return
                
            #robot senses a cup to the right,
            #turn right to center cup
            if right > 400:
                turnRight(.2,.5)
                stop() 
                beep(2,850)
                return
main()