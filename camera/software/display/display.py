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
  def __init__(self, main):
    self.active_img = None
    self.base_path = "/home/pi/pi-zero-hq-cam/camera/software/display/images/"
    self.font_path = "/home/pi/pi-zero-hq-cam/camera/software/display/"
    self.menu_path = "/home/pi/pi-zero-hq-cam/camera/software/menu/"

    # setup OLED
    Device_Init(main)

  def start_menu(self):
    print('start menu')

  def display_image(self, img_path):
    image = Image.open(img_path)
    Display_Image(image)

  def display_buffer(self, buffer):
    Display_Buffer(buffer)

  def clear_screen(self):
    Clear_Screen()

  def show_boot_scene(self):
    boot_img_path = self.base_path + "/boot.jpg"
    self.active_img = Image.open(boot_img_path)
    self.display_image(boot_img_path)
    time.sleep(3)
    self.clear_screen()
  
  def show_home_sprite(self):
    home_sprite_path = self.menu_path + "/menu-sprites/home.jpg"
    self.active_img = Image.open(home_sprite_path)
    self.display_image(home_sprite_path)
    self.draw_active_square("bluetooth")

  def draw_square(tl_coord, br_coord):
      print('method')

  # draw same square but black
  def undraw_active_square(self, cur_icon):
    draw = self.active_img # no err check

    if (cur_icon == "bluetooth"):
      draw.line([(15, 100), (41, 100)], fill = "MAGENTA", width = 2)
    elif (cur_icon == "telemetry"):
      draw.line([(21, 107), (41, 107)], fill = "MAGENTA", width = 2)
    elif (cur_icon == "files"):
      draw.line([(21, 107), (41, 107)], fill = "MAGENTA", width = 2)
    else:
      draw.line([(21, 107), (41, 107)], fill = "MAGENTA", width = 2)

  def draw_active_square(self, which_icon):
    # paste lol cool https://stackoverflow.com/a/2563883
    base_img = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(base_img)
    base_img.paste(self.active_img)

    if (which_icon == "bluetooth"):
      draw.line([(5, 98), (25, 98)], fill = "MAGENTA", width = 2)
      draw.line([(5, 125), (25, 125)], fill = "MAGENTA", width = 2)
    elif (which_icon == "telemetry"):
      draw.line([(21, 107), (41, 107)], fill = "MAGENTA", width = 2)
    elif (which_icon == "files"):
      draw.line([(21, 107), (41, 107)], fill = "MAGENTA", width = 2)
    else:
      draw.line([(21, 107), (41, 107)], fill = "MAGENTA", width = 2)

    Display_Image(base_img)

  def draw_text(self, text):
    image = Image.new("RGB", (128, 128), "BLACK")
    self.active_img = image
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(self.font_path + "cambriab.ttf", 12)

    draw.text((0, 96), text, fill = "WHITE", font = font)

    Display_Image(image)

    time.sleep(2)

  def set_center_home_text(self, text):
    base_img = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(base_img)
    base_img.paste(self.active_img)

    draw.line([(0, 20), [128, 90]], fill = "BLACK", width = 70)
    # math to shift left text based on length
    font = ImageFont.truetype(self.font_path + "cambriab.ttf", 18)
    draw.text((0, 45), text, fill = "WHITE", font = font)

    Display_Image(base_img)
