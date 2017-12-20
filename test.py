#!/usr/bin/python
#


# Import required libraries
#import sys
import time
import RPi.GPIO as GPIO
from PowerLock import PowerLock
from fishfeeder2 import FishFeeder2



########################################################
# Function shutdown
########################################################


def shutdown():
  GPIO.cleanup()
  print
  print "Bye!"  

# End Function shutdown



########################################################
#
# Main
#
########################################################

try:
  foodDoorPinA = 2
  foodDoorPinB = 3
  laserPin    = 4
# 17

  foodLowPin  = 24

  fishFeeder = FishFeeder2(foodDoorPinA, foodDoorPinB, foodLowPin, laserPin)

  fishFeeder.init()
  fishFeeder.feedOneServing()

  fishFeeder.checkFoodLow()
  print "Food low = ", fishFeeder.isFoodLow

# End try

except KeyboardInterrupt:
  # This statement is meaningless other than it allows the program to
  # drop down to the next line.
  print "Keyboard Interrupt"

# End except

shutdown()

########################################################
#
# End Main
#
########################################################
