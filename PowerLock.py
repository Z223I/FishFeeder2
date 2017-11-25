#!/usr/bin/python
#


# Import required libraries
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
# Function lock
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
