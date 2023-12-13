import time

#--------------Driver Library-----------------#
import RPi.GPIO as GPIO
import OLED_Driver as OLED

#--------------Image Library---------------#
from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

class Display:
  def __init__(self):
    self.base_path = "/home/pi/pi-zero-hq-cam/camera/software/display-images"
    print('init')

  def display_image(img_path):
    image = Image.open(img_path)
    OLED.Display_Image(image)

  def clear_screen():
    OLED.Clear_Screen()

  def show_boot_scene(self):
    boot_img_path = self.base_path + "/boot.jpg"
    self.display_image(boot_img_path)
    time.sleep(3)
    self.display.clear_screen()
