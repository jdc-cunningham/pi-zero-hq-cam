import time

from picamera2 import Picamera2

class Camera:
  def __init__(self, display):
    self.picam2 = Picamera2()
    self.small_config = self.picam2.create_still_configuration(main={"size": (128, 128)})
    self.full_res_config = self.picam2.create_still_configuration()
    self.picam2.configure(self.small_config)
    self.live_preview_active = False
    self.live_preview_start = 0 # time.time() to keep at 10 seconds max unless interaction
    self.img_base_path = "/home/pi/pi-zero-hq-cam/camera/software/captured-media/"

  def change_mode(self, mode):
    if (mode == "full"):
      self.picam2.configure(self.full_res_config)
    else:
      self.picam2.configure(self.small_config)

  def start_live_preview(self):
    self.live_preview_active = True
    self.live_preview_active = time.time()
    self.display.clear_screen()

    while (self.live_preview_active):
      pil_img = self.picam2.capture_image()
      self.display.Display_Image(pil_img)

      if (time.time() > self.live_preview_start - 10):
        self.live_preview_active = False


  def stop_live_preview(self):
    self.live_preview_active = False

  def take_photo(self):
    self.change_mode('full')
    self.picam2.capture_file(self.img_base_path + str(time.time()).split(".")[0] + ".jpg")
    self.live_preview_start = time.time() # keep 10 sec clock running
