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
    self.small_res_config = self.picam2.create_still_configuration(main={"size": (128, 128)}) # should not be a square
    self.zoom_4x_config = self.picam2.create_still_configuration(main={"size": (1014, 760)})
    self.full_res_config = self.picam2.create_still_configuration() # also same as 16x
    self.zoom_level = 1 # 1, 4 capped to 4 because 16x would be way too much (OLED refresh rate and vibration of hand)
    self.pan_offset = [0, 0] # depends on zoom level, should be at center crop
    self.crop = [128, 128]

    self.picam2.configure(self.small_res_config)

  def start(self):
    self.picam2.start()

  def stop(self):
    self.picam2.stop()

  def change_mode(self, mode):
    if (mode == "full" or mode == "zoom 16x"):
      self.picam2.switch_mode(self.full_res_config)
    elif (mode == "zoom 4x"):
      self.picam2.switch_mode(self.zoom_4x_config)
    else:
      self.picam2.switch_mode(self.small_res_config)

  # here you can crop/pan the image before it is displayed on the OLED
  def check_mod(self, pil_img):
    if (self.zoom_level > 1):
      if (self.zoom_level == 4):
        self.pan_offset = [443, 316] # based on (1014/2) - (128/2)
        return pil_img.crop((self.pan_offset[0], self.pan_offset[1], self.pan_offset[0] + self.crop[0], self.pan_offset[1] + self.crop[1]))
    else:
      return pil_img

  def live_preview(self):
    self.display.clear_screen()

    while (self.live_preview_active):
      if (not self.live_preview_pause):
        pil_img = self.picam2.capture_image()
        pil_img = self.check_mod(pil_img) # bad name
        self.display.display_buffer(pil_img.load())

      # after 1 min turn live preview off
      if (time.time() > self.live_preview_start + 60 and not self.live_preview_pause):
        self.live_preview_pause = True
        self.zoom_level = 1
        self.pan_offset = [0, 0]
        self.display.clear_screen()
        self.change_mode("full")
        self.display.start_menu()

  def start_live_preview(self):
    Thread(target=self.live_preview).start()

  def take_photo(self):
    img_path = self.img_base_path + str(time.time()).split(".")[0] + ".jpg"
    self.change_mode("full")
    self.picam2.capture_file(img_path)
    self.change_mode("small")

  def reset_preview_time(self):
    self.live_preview_start = time.time()

  def set_live_preview_active(self, preview_active):
    if (preview_active):
      self.reset_preview_time()
      self.live_preview_pause = False
      self.live_preview_active = True
      self.main.live_preview_active = True
    else:
      self.live_preview_pause = True
      self.main.live_preview_active = False

  def handle_shutter(self):
    # start live preview again
    if (self.live_preview_active and self.live_preview_pause):
      self.set_live_preview_active(True)
      time.sleep(0.5)
      return

    if (not self.live_preview_active):
      self.set_live_preview_active(True)
      self.start_live_preview()
    else:
      self.set_live_preview_active(False)
      self.display.clear_screen()
      self.display.draw_text("Taking photo...")
      self.take_photo()
      self.display.clear_screen()
      self.display.draw_text("Photo captured")
      self.display.clear_screen()
      self.set_live_preview_active(True)

  def zoom_in(self):
    if (self.zoom_level == 1):
      self.zoom_level = 4
      self.change_mode("zoom 4x")

  def zoom_out(self):
    if (self.zoom_level == 4):
      self.zoom_level = 1
      self.change_mode("small")

  def handle_zoom(self, button):
    self.reset_preview_time()

    if (button == "CENTER"):
      self.zoom_in()
    else:
      self.zoom_out()

  def handle_pan(self, button):
    if (button == "UP"):
      print('pan up')
    if (button == "LEFT"):
      print('pan left')
    if (button == "RIGHT"):
      print('pan right')
    if (button == "DOWN"):
      print('pan down')
