import os
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
base_path = os.getcwd() # root of repo eg. /software/ since main.py calls process

battery_sprite_path = base_path + "/menu/menu-sprites/battery_25_15.jpg"
folder_sprite_path = base_path + "/menu/menu-sprites/folder_21_18.jpg"
gear_sprite_path = base_path + "/menu/menu-sprites/gear_23_20.jpg"

small_font = ImageFont.truetype(base_path + "/display/alt-font.ttc", 13)
large_font = ImageFont.truetype(base_path + "/display/alt-font.ttc", 16)

class Display:
  def __init__(self, pi_ver, utils):
    self.active_img = None
    self.active_icon = None
    self.utils = utils
    self.file_count = self.utils.get_file_count() # maybe shouldn't be here

    # setup OLED
    Device_Init(pi_ver)
  
  def render_menu_base(self, center_text = "Camera on"):
    image = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(image)

    draw.text((7, 3), "video", fill = "WHITE", font = small_font)
    draw.text((7, 105), "Auto", fill = "WHITE", font = small_font)
    # manual photography mode
    # draw.text((7, 90), "S: 1/60", fill = "WHITE", font = small_font)
    # draw.text((7, 105), "E: 100", fill = "WHITE", font = small_font)
    draw.text((22, 48), center_text, fill = "WHITE", font = large_font)
    draw.text((66, 3), "3 hrs", fill = "WHITE", font = small_font)
    draw.text((60, 103), str(self.file_count), fill = "WHITE", font = small_font)

    battery_icon = Image.open(battery_sprite_path)
    folder_icon = Image.open(folder_sprite_path)
    gear_icon = Image.open(gear_sprite_path)

    image.paste(battery_icon, (98, 5))
    image.paste(folder_icon, (77, 103))
    image.paste(gear_icon, (101, 102))

    return image

  def start_menu(self):
    menu_base = self.render_menu_base()

    Display_Image(menu_base)

  def display_image(self, img_path):
    image = Image.open(img_path)
    Display_Image(image)

  def display_buffer(self, buffer):
    Display_Buffer(buffer)

  def clear_screen(self):
    Clear_Screen()

  def show_boot_scene(self):
    boot_img_path = base_path + "/display/images/boot.jpg"
    self.active_img = Image.open(boot_img_path)
    self.display_image(boot_img_path)
    time.sleep(3)
    self.clear_screen()

  def set_menu_center_text(self, draw, text, x = 22, y = 48):
    draw.text((x, y), text, fill = "WHITE", font = large_font)

  def draw_active_icon(self, icon_name):
    image = self.render_menu_base("")
    draw = ImageDraw.Draw(image)

    if (icon_name == "Files"):
      draw.line([(60, 121), (98, 121)], fill = "MAGENTA", width = 2)
      self.set_menu_center_text(draw, "Files")

    if (icon_name == "Camera Settings"):
      draw.line([(7, 121), (34, 121)], fill = "MAGENTA", width = 2)
      self.set_menu_center_text(draw, "Camera Settings", 5)

    if (icon_name == "Photo Video Toggle"):
      draw.line([(7, 22), (34, 22)], fill = "MAGENTA", width = 2)
      self.set_menu_center_text(draw, "Toggle Mode")

    if (icon_name == "Settings"):
      draw.line([(101, 122), (124, 122)], fill = "MAGENTA", width = 2)
      self.set_menu_center_text(draw, "Settings")
    
    Display_Image(image)