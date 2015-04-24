# findPink.py is a program written in Python
# using The Calico Project along with the 
# Scribbler 2 robot. Drives the Scribbler
# around obstacles in search for a goal
# which is a pink cup.

# Authors: Michael Arteaga/Josh Levine
# Date: April 2015

from Myro import *
import sys #used to quit the program altogether

# Runs until Scribber finds the pink cup
# Michael
def main():
    while True:
        center = findCenter()
        if (center == 127.5): # no cup
            turnLeft(.3,.1)
        elif (center < 110):  # cup is on left
            turnLeft(.3,.1)
        elif (center > 134):  # cup is on right
            turnRight(.3,.1)
        else:
            findPinkCup()     # drive

# findPinkCup() drives towards the goal
# Josh
def findPinkCup():
    left, center, right = getObstacle()
    forward(-.2)
    if center > 950:
            if left < 100:
                if right < 100:
                    stop()
                    isPink()
                                      
    if center > 950:
        #robot senses a cup to the left,
        #turn left to center cup
        if left > 400:
            turnLeft(.2,.5)
            stop()
            isPink()
            
        #robot senses a cup to the right,
        #turn right to center cup
        if right > 400:
            turnRight(.2,.5)
            stop() 
            isPink()
            
# isPink() determines whether the obstacle
# in front is pink or not. 
# Michael      
def isPink():
    pic = takePicture()
    show(pic) #to see what scribbler sees
    pixel = getPixel(pic, 128,96) # gets center pixel
    red, green, blue = getRGB(pixel)
    if (red > 225 and green < 150): 
        beep(1,1000) # goal
        sys.exit(0)  # force quit
    else:
        avoid()     # crash collision w/ obstacle 

# avoid() is a helper method that is called
# to drive around the obstacle.
# Josh
def avoid():
    left, center, right = getObstacle()
    if(right > 200):
        turnLeft(.5,1.25)
        forward(-.5,2.75)
        turnRight(.5,1.75)
    elif(left > 200):
        turnRight(.5,1.25)
        forward(-.5,2.75)
        turnLeft(.5,1.4)
        
#Finds the blob in picture and
#calculates the center of the blob
#returns a float - center    
# Michael
def findCenter():
    pic = takePicture("blob")
    show(pic)
    left = 255
    right = 0
    for x in range(255):
        for y in range(191):
            pixel = getPixel(pic, x, y)
            red, green, blue = getRGB(pixel)
            if (red > 0 and x > right):
                right = x
            if (red > 0 and x < left):
                left = x
    #print(left,right)
    if (left+right > 0):
        center = (left+right)/2
    else:
        center = 0
    #print(center)  #shows where the pink cup is
    return center
    
main()