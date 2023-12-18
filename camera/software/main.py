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

import time, os
import RPi.GPIO as GPIO

from threading import Thread
from buttons.buttons import Buttons
# from battery.battery import BattDb
from camera.camera import Camera
from display.display import Display
# from menu.menu import Menu

class Main:
  def __init__(self):
    self.on = True # what
    self.img_base_path = "/home/pi/pi-zero-hq-cam/camera/software/captured-media/"
    self.display = Display()
    self.display.show_boot_scene()
    self.live_preview_active = False
    self.camera = Camera(self.display, self)
    self.picam2.start()
    self.camera_on = False
    self.buttons = Buttons(self.button_pressed)
    self.buttons_thread = Thread(target=self.buttons.start)
    self.buttons_thread.start()
    self.live_preview_thread = None
    self.live_preview_start = 0
    self.shutter_event_processing = False
    self.photo_taken_path = None
    self.display.draw_text("Camera on") # set last so everything is ready

    # keep main running
    while (self.on):
      print('on') # replace with battery check
      time.sleep(60)

  # def set_photo_taken_path(self, path):
  #   self.photo_taken_path = path

  def button_pressed(self, button):
    if (button == "SHUTTER"):
      if (not self.live_preview_active):
        self.live_preview_active = True
        self.live_preview_start = time.time()
        self.camera.start_live_preview(self.live_preview_active, self.live_preview_start)
      else:
        self.camera.take_photo(self.set_last_photo_path)
        self.live_preview_active = False
        self.display.clear_screen()
        self.display.draw_text("Photo captured")
        self.display.clear_screen()

Main()
