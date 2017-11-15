#!/usr/bin/python
#


# Import required libraries
#import sys
#import time
import RPi.GPIO as GPIO




########################################################
#
# Class FishFeeder2
#
########################################################

class FishFeeder2():

  # Define GPIO signals to use
  # Physical pins 11,15,16,18
  # GPIO17, GPIO18, GPIO22, GPIO23
  isFoodLow = False

########################################################
# Function __init__
########################################################

  def __init__(self):
    print "__init__"
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
#    GPIO.output(pin, False)

    isFoodLow = False
# End Function init


########################################################
# Function feedOneServing
########################################################

  def feedOneServing(self):
    #print "feedOneServing"
    print "Feeding one serving..."

########################################################
# End Function feedOneServing
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
  fishFeeder = FishFeeder2()

  fishFeeder.init()
  fishFeeder.feedOneServing()
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
