import os

class Utils:
  def __init__(self):
    self.pi_ver = 1 # or 2 determine

  # need this for OLED max SPI speed (refresh)
  def get_pi_ver(self):
    self.pi_ver = 2 if (os.system('less /proc/cpupinfo | grep processor | wc -l') > 2) else 1 # lol this is great
