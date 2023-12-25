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

from buttons.buttons import Buttons
# from battery.battery import BattDb
from camera.camera import Camera
from menu.menu import Menu
from display.display import Display
from utils.utils import Utils

class Main:
  def __init__(self):
    self.on = True
    self.display = None
    self.controls = None
    self.utils = None
    self.menu = None
    self.camera = None

    self.startup()

    # keep main running
    while (self.on):
      print('on') # replace with battery check
      time.sleep(60)

  def startup(self):
    self.utils = Utils()
    self.display = Display(self.utils.pi_ver, self.utils)
    self.camera = Camera(self.display, self)
    self.menu = Menu(self.display, self.camera)
    self.display.show_boot_scene()
    self.display.start_menu()
    self.controls = Buttons(self.button_pressed)

    self.camera.start()
    self.controls.start()

  def button_pressed(self, button):
    if (button == "SHUTTER"):
      self.camera.handle_shutter()
    else:
      self.menu.update_state(button)

Main()
