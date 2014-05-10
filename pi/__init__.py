import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def receive_ping():
   print "Ping received"
   return True

def send_high(pin, duration=1):
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(duration)
  GPIO.output(pin, GPIO.LOW)
