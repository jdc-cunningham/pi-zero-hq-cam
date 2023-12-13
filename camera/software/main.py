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
    self.display = Display(self.get_photo_count)
    self.display.show_boot_scene()
    self.live_preview_active = False
    self.camera = Camera(self.display)
    self.buttons = Buttons(self.button_pressed)
    self.buttons_thread = Thread(target=self.buttons.start)
    self.buttons_thread.start()
    self.live_preview_thread = None
    self.live_preview_start = 0
    self.shutter_event_processing = False

    # keep main running
    while (self.on):
      print('on') # replace with battery check
      time.sleep(60)

  # https://stackoverflow.com/a/8311376/2710227
  def get_photo_count(self):
    _, _, files = next(os.walk(self.img_base_path))
    return len(files)

  def start_live_preview(self):
    self.live_preview_active = True
    self.live_preview_start = time.time()
    self.live_preview_thread = Thread(target=self.camera.start_live_preview, args=(self.live_preview_active, self.live_preview_start))
    self.live_preview_thread.start()
    self.shutter_event_processing = False

  def button_pressed(self, button):
    print(button)
    print(self.live_preview_active)

    if (button == "SHUTTER" and not self.shutter_event_processing):
      self.shutter_event_processing = True

      if (not self.live_preview_active):
        self.start_live_preview()
      else:
        self.live_preview_active = False
        time.sleep(1.5)
        self.display.clear_screen()
        time.sleep(2)
        self.camera.take_photo()
        time.sleep(5)
        self.start_live_preview()

Main()
