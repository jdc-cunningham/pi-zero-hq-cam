# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

import RPi.GPIO as GPIO
import time

class Buttons():
  def __init__(self, callback = None):
    self.exit = False
    self.callback = callback

    # already set as BCM by OLED

    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # UP
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # LEFT
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # CENTER
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # RIGHT
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # DOWN
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # BACK
    GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # SHUTTER

  # listen for input
  def start(self):
    while True:
      if self.exit: return False

      if GPIO.input(4) == GPIO.HIGH:
        self.callback("UP")
      if GPIO.input(21) == GPIO.HIGH:
        self.callback("LEFT")
      if GPIO.input(22) == GPIO.HIGH:
        self.callback("CENTER")
      if GPIO.input(23) == GPIO.HIGH:
        self.callback("RIGHT")
      if GPIO.input(24) == GPIO.HIGH:
        self.callback("DOWN")
      if GPIO.input(7) == GPIO.HIGH:
        self.callback("BACK")
      if GPIO.input(1) == GPIO.HIGH:
        self.callback("SHUTTER")

      time.sleep(0.05)
