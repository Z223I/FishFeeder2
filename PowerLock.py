#!/usr/bin/python
#


# Import required libraries
import time
import RPi.GPIO as GPIO




########################################################
#
# Class PowerLock
#
# This class manipulates an automotive power lock.
#
# It takes two pins to manipulate the power lock because
# the polarity has to be changed to switch between
# between states.
#
########################################################

class PowerLock():


########################################################
# Function __init__
########################################################

  def __init__(self, _powerLockPinA, _powerLockPinB):
    print "__init__"

    # Define GPIO signals to use
    # Physical pins 11,15,16,18
    # GPIO17, GPIO18, GPIO22, GPIO23
    
    self.powerLockPinA = _powerLockPinA
    self.powerLockPinB = _powerLockPinB

    self.powerDelay = .2
# End Function __init__


########################################################
# Function init
########################################################

  def init(self):
    print "init"
  
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Set pins to output and initialize them to false.
    GPIO.setup(self.powerLockPinA, GPIO.OUT)
    GPIO.output(self.powerLockPinA, False)
    GPIO.setup(self.powerLockPinB, GPIO.OUT)
    GPIO.output(self.powerLockPinB, False)

# End Function init



########################################################
# Function cycle
########################################################

  def cycle(self):
    self.unlock()
    self.lock()

########################################################
# End Function cycle
########################################################



########################################################
# Function lock
########################################################

  def lock(self):

    GPIO.output(self.powerLockPinA, True)
    GPIO.output(self.powerLockPinB, False)

    time.sleep(self.powerDelay)

    self.powerOff()

########################################################
# End Function lock
########################################################



########################################################
# Function powerOff
########################################################

  def powerOff(self):

    # Power off both pins
    GPIO.output(self.powerLockPinA, False)
    GPIO.output(self.powerLockPinB, False)


########################################################
# End Function powerOff
########################################################



########################################################
# Function setPowerDelay
########################################################

  def setPowerDelay(self, _powerDelay):

    self.powerDelay = _powerDelay

########################################################
# End Function setPowerDelay
########################################################



########################################################
# Function unlock
########################################################

  def unlock(self):

    GPIO.output(self.powerLockPinA, False)
    GPIO.output(self.powerLockPinB, True)

    time.sleep(self.powerDelay)

    self.powerOff()

########################################################
# End Function unlock
########################################################

########################################################
#
# End class PowerLock
#
########################################################
