import time

#--------------Driver Library-----------------#
import RPi.GPIO as GPIO
from .OLED_Driver import Device_Init, Display_Image, Clear_Screen, Display_Buffer

#--------------Image Library------------------#
from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

#--------------Assets------------------#
battery_sprite_path = "../menu/menu-sprites/battery_25_15.jpg"
folder_sprite_path = "../menu/menu-sprites/folder_21_18.jpg"
gear_sprite_path = "../menu/menu-sprites/gear_23_20.jpg"

base_path = "../display/images/"
font_path = "../display/"
menu_path = "../menu/"

small_font = ImageFont.truetype(font_path + "alt-font.ttc", 13)
large_font = ImageFont.truetype(font_path + "alt-font.ttc", 16)

class Display:
  def __init__(self, main):
    self.active_img = None

    # setup OLED
    Device_Init(main)

  def start_menu(self):
    image = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(image)

    small_font = ImageFont.truetype(font_path + "alt-font.ttc", 13)
    large_font = ImageFont.truetype(font_path + "alt-font.ttc", 16)

    draw.text((7, 3), "video", fill = "WHITE", font = small_font)
    draw.text((7, 90), "S: 1/60", fill = "WHITE", font = small_font)
    draw.text((7, 105), "E: 100", fill = "WHITE", font = small_font)
    draw.text((22, 48), "Camera on", fill = "WHITE", font = large_font)
    draw.text((66, 3), "3 hrs", fill = "WHITE", font = small_font)
    draw.text((60, 103), "24", fill = "WHITE", font = small_font)

    battery_icon = Image.open(battery_sprite_path)
    folder_icon = Image.open(folder_sprite_path)
    gear_icon = Image.open(gear_sprite_path)

    image.paste(battery_icon, (98, 5))
    image.paste(folder_icon, (77, 103))
    image.paste(gear_icon, (101, 103))

    Display_Image(image)

  def display_image(self, img_path):
    image = Image.open(img_path)
    Display_Image(image)

  def display_buffer(self, buffer):
    Display_Buffer(buffer)

  def clear_screen(self):
    Clear_Screen()

  def show_boot_scene(self):
    boot_img_path = base_path + "/boot.jpg"
    self.active_img = Image.open(boot_img_path)
    self.display_image(boot_img_path)
    time.sleep(3)
    self.clear_screen()
  
  def show_home_sprite(self):
    home_sprite_path = self.menu_path + "/menu-sprites/home.jpg"
    self.active_img = Image.open(home_sprite_path)
    self.display_image(home_sprite_path)
