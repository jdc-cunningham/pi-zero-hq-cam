# https://github.com/jdc-cunningham/ml-hat-cam/blob/main/code/dpad/dpad.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # UP
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # LEFT
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # CENTER
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # RIGHT
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # DOWN
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # BACK
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # SHUTTER

while True:
  if GPIO.input(4) == GPIO.HIGH:
    print("UP")
  if GPIO.input(21) == GPIO.HIGH:
    print("LEFT")
  if GPIO.input(22) == GPIO.HIGH:
    print("CENTER")
  if GPIO.input(23) == GPIO.HIGH:
    print("RIGHT")
  if GPIO.input(24) == GPIO.HIGH:
    print("DOWN")
  if GPIO.input(20) == GPIO.HIGH:
    print("BACK")
  if GPIO.input(1) == GPIO.HIGH:
    print("SHUTTER")

  time.sleep(0.05)