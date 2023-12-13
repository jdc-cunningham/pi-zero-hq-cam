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
  def __init__(self, get_photo_count):
    self.base_path = "/home/pi/pi-zero-hq-cam/camera/software/display-images"
    self.file_count = get_photo_count()
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
    
    # list files
    self.display.draw_text("file count: " + self.file_count)

  def draw_text(self, text):
    image = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('cambriab.ttf',24)

    draw.text((55, 96), text, fill = "WHITE", font = font)

    self.display_image(image)