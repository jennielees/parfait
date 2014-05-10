# Using libraries/flow from https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/
# Note that GPIO requires running scripts (including rqworker) as root.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DEFAULT_PIN = 8

def receive_ping():
   print "Ping received"
   send_high()
   return True

def send_high(pin=DEFAULT_PIN, duration=1):
  print "Lighting up pin %s for %s seconds." % (pin, duration)
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(duration)
  GPIO.output(pin, GPIO.LOW)

if __name__=="__main__":
  # Command line test.
  send_high()
