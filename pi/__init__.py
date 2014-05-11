# Using libraries/flow from https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/
# Note that GPIO requires running scripts (including rqworker) as root.

import RPi.GPIO as GPIO
import time
from app import helper

GPIO.setmode(GPIO.BCM)
OUTPUT_PIN = 8
INPUT_PIN = 18

def receive_ping():
   print "Ping received"
   send_high()
   return True

def send_high(pin=OUTPUT_PIN, duration=1):
  print "Lighting up pin %s for %s seconds." % (pin, duration)
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(duration)
  GPIO.output(pin, GPIO.LOW)

def listen_for_IR(pin=INPUT_PIN):
  print "Listening for IR"
  GPIO.setup(pin, GPIO.IN)
  input = GPIO.input(pin)
  while True:
    prev_input = input
    input = GPIO.input(pin)
    if input is False:
      # We've received a signal via IR
      print "Received IR signal on pin %s" % pin
#      send_high()
      helper.create_job()
    time.sleep(0.05)

if __name__=="__main__":
  # Command line test.
  listen_for_IR()
#  send_high()
