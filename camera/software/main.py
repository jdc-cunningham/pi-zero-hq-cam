'''
- boots
  - ask if charged (battery)
  - idle
    (click center button or shutter) show camera pass through, wait for buttons, maybe overlay telemetry/horizon,
    sample imu in separate thread
  - shutter (photo)
  - non-center d-pad button (show/navigate menu)
  - CRON sqlite db counter for battery consumption
'''

# import os, sys, time

from threading import Thread

from buttons.buttons import Buttons
from battery.battery import BattDb
from camera.camera import Camera
from display.display import Display
from menu.menu import Menu

def button_pressed(button):
  print(button)

control = Buttons(button_pressed)
control.start()
