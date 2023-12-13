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

import time

from threading import Thread

from buttons.buttons import Buttons
# from battery.battery import BattDb
from camera.camera import Camera
from display.display import Display
# from menu.menu import Menu

class Main:
  def __init__(self):
    self.on = True # what
    self.display = Display()
    self.display.show_boot_scene()
    self.live_preview_active = False
    self.camera = Camera(self.display, self.live_preview_active)
    self.buttons = Buttons(self.button_pressed)
    self.buttons_thread = Thread(target=self.buttons.start)
    self.buttons_thread.start()

    # keep main running
    while (self.on):
      print('on') # replace with battery check
      time.sleep(60)

  def button_pressed(self, button):
    print(button)

    if (button == "SHUTTER"):
      if (not self.live_preview_active):
        self.camera.start_live_preview()

      self.camera.take_photo()

Main()
