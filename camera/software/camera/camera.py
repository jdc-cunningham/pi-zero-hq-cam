import time

from picamera2 import Picamera2

class Camera:
  def __init__(self, display, main):
    self.main = main
    self.display = display
    self.picam2 = Picamera2()
    self.small_config = self.picam2.create_still_configuration(main={"size": (128, 128)})
    self.full_res_config = self.picam2.create_still_configuration()
    self.picam2.configure(self.full_res_config)
    self.img_base_path = "/home/pi/pi-zero-hq-cam/camera/software/captured-media/"

  def start(self, main):
    self.picam2.start()
    main.camera_on = True

  def change_mode(self, mode):
    if (mode == "full"):
      self.picam2.switch_mode(self.full_res_config)
    else:
      self.picam2.switch_mode(self.small_config)

  def start_live_preview(self, live_preview_active, live_preview_start):
    self.display.clear_screen()

    while (live_preview_active):
      pil_img = self.picam2.capture_image()
      self.display.display_buffer(pil_img.load())

      if (time.time() < live_preview_start - 10):
        self.main.live_preview_active = False
        break

  def take_photo(self, set_last_photo_path):
    img_path = self.img_base_path + str(time.time()).split(".")[0] + ".jpg"
    self.picam2.capture_file(img_path)
    set_last_photo_path(img_path)
