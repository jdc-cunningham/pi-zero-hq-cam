import os, time

from threading import Thread
from picamera2 import Picamera2

class Camera:
  def __init__(self, display, main):
    self.display = display
    self.main = main
    self.manual_mode = False
    self.img_base_path = os.getcwd() + "/captured-media/"
    self.live_preview_active = False
    self.live_preview_start = 0
    self.live_preview_pause = False
    self.picam2 = Picamera2()
    self.small_res_config = self.picam2.create_still_configuration(main={"size": (128, 128)})
    self.full_res_config = self.picam2.create_still_configuration()

    self.picam2.configure(self.small_res_config)

  def start(self):
    self.picam2.start()

  def stop(self):
    self.picam2.stop()

  def change_mode(self, mode):
    if (mode == "full"):
      self.picam2.switch_mode(self.full_res_config)
    else:
      self.picam2.switch_mode(self.small_res_config)

  def live_preview(self):
    self.display.clear_screen()

    while (self.live_preview_active):
      if (not self.live_preview_pause):
        pil_img = self.picam2.capture_image()
        self.display.display_buffer(pil_img.load())

      # after 10 seconds turn off
      if (time.time() > self.live_preview_start + 60 and not self.live_preview_pause):
        self.live_preview_pause = True
        self.display.clear_screen()
        self.display.start_menu()

  def start_live_preview(self):
    Thread(target=self.live_preview).start()

  def take_photo(self):
    img_path = self.img_base_path + str(time.time()).split(".")[0] + ".jpg"
    self.change_mode("full")
    self.picam2.capture_file(img_path)
    self.change_mode("small")

  def handle_shutter(self):
    if (self.live_preview_active and self.live_preview_pause):
      self.live_preview_start = time.time()
      self.live_preview_pause = False
      time.sleep(0.5)
      return

    if (not self.live_preview_active):
      self.live_preview_active = True
      self.live_preview_start = time.time()
      self.start_live_preview()
    else:
      self.live_preview_pause = True
      self.display.clear_screen()
      self.display.draw_text("Taking photo...")
      self.take_photo()
      self.display.clear_screen()
      self.display.draw_text("Photo captured")
      self.display.clear_screen()
      self.live_preview_pause = False # keep going or 10 second cutoff kicks in
      self.live_preview_start = time.time() # reset counter