#!/usr/bin/python
#


# Import required libraries
#import sys
import time
import RPi.GPIO as GPIO




########################################################
#
# Class FishFeeder2
#
########################################################

class FishFeeder2():


########################################################
# Function __init__
########################################################

  def __init__(self, _foodDoorPinA,_foodDoorPinB, _foodLowPin, _laserPin):
    print "__init__"

    # Define GPIO signals to use
    # Physical pins 11,15,16,18
    # GPIO17, GPIO18, GPIO22, GPIO23
    
    self.foodDoorPinA = _foodDoorPinA
    self.foodDoorPinB = _foodDoorPinB
    self.foodLowPin  = _foodLowPin
    self.laserPin    = _laserPin
    self.isFoodLow   = False
# End Function __init__


########################################################
# Function init
########################################################

  def init(self):
    print "init"
  
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Set all pins as output
#    for pin in self.StepPins:
#      print "Setup pins"
#      GPIO.setup(pin,GPIO.OUT)
#      GPIO.output(pin, False)

    GPIO.setup(foodDoorPinA, GPIO.OUT)
    GPIO.output(foodDoorPinA, False)
    GPIO.setup(foodDoorPinB, GPIO.OUT)
    GPIO.output(foodDoorPinB, False)

    GPIO.setup(laserPin, GPIO.OUT)
    GPIO.output(laserPin, False)

    GPIO.setup(foodLowPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Pull low
    #GPIO.output(foodDoorPin, False)

    isFoodLow = False
# End Function init


########################################################
# Function feedOneServing
########################################################

  def feedOneServing(self):
    #print "feedOneServing"
    print "Feeding one serving..."
    foodDoorPinA = True
    foodDoorPinB = False
    time.sleep(.2)
    foodDoorPinA = False
    foodDoorPinB = True
    time.sleep(.2)
    foodDoorPinB = False

########################################################
# End Function feedOneServing
########################################################


########################################################
# Function checkFoodLow
########################################################

  def checkFoodLow(self):
    print "Check food low..."

    # Turn on laser
    GPIO.output(self.laserPin, True)
    time.sleep(.5)

    # Read laser detector
    isFoodLow = GPIO.input(foodLowPin)

    # Turn off laser
    GPIO.output(self.laserPin, False)


########################################################
# End Function checkFoodLow
########################################################


########################################################
#
# End class FishFeeder2
#
########################################################


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
  foodDoorPinA = 17
  foodDoorPinB = 18
  laserPin    = 22
# 23

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
