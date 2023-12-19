import time

#--------------Driver Library-----------------#
import RPi.GPIO as GPIO
from .OLED_Driver import Device_Init, Display_Image, Clear_Screen, Display_Buffer

#--------------Image Library---------------#
from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

class Display:
  def __init__(self):
    self.base_path = "/home/pi/pi-zero-hq-cam/camera/software/display-images/"
    self.font_path = "/home/pi/pi-zero-hq-cam/camera/software/display/"
    Device_Init()

  def display_image(self, img_path):
    image = Image.open(img_path)
    Display_Image(image)

  def display_buffer(self, buffer):
    Display_Buffer(buffer)

  def clear_screen(self):
    Clear_Screen()

  def show_boot_scene(self):
    boot_img_path = self.base_path + "/boot.jpg"
    self.display_image(boot_img_path)
    time.sleep(3)
    self.clear_screen()

  def draw_text(self, text):
    image = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(self.font_path + "cambriab.ttf", 12)

    draw.text((0, 96), text, fill = "WHITE", font = font)

    Display_Image(image)

    time.sleep(2)