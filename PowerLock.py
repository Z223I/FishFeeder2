#!/usr/bin/python
#


# Import required libraries
#import sys
import time
import RPi.GPIO as GPIO




########################################################
#
# Class PowerLock
#
########################################################

class PowerLock():


########################################################
# Function __init__
########################################################

  def __init__(self, _powerLockPinA,_powerLockPinB):
    print "__init__"

    # Define GPIO signals to use
    # Physical pins 11,15,16,18
    # GPIO17, GPIO18, GPIO22, GPIO23
    
    self.powerLockPinA = _powerLockPinA
    self.powerLockPinB = _powerLockPinB
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

    GPIO.setup(powerLockPinA, GPIO.OUT)
    GPIO.output(powerLockPinA, False)
    GPIO.setup(powerLockPinB, GPIO.OUT)
    GPIO.output(powerLockPinB, False)

# End Function init


########################################################
# Function cycle
########################################################



# TODO this should be calling GPIO.output



  def cycle(self):
    #print "feedOneServing"
    print "Feeding one serving..."
    powerLockPinA = True
    GPIO.output(powerLockPinA, True)


    powerLockPinB = False
    GPIO.output(powerLockPinB, False)

    time.sleep(.2)


    powerLockPinA = False
    GPIO.output(powerLockPinA, False)


    powerLockPinB = True
    GPIO.output(powerLockPinB, True)


    time.sleep(.2)


    powerLockPinB = False
    GPIO.output(powerLockPinB, False)

########################################################
# End Function cycle
########################################################


########################################################
#
# End class PowerLock
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
  powerLockPinA = 17
  powerLockPinB = 18

  powerLock = PowerLock(powerLockPinA, powerLockPinB)

  powerLock.init()
  powerLock.cycle()

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
