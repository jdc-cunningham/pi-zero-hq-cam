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

# temporary (lol)
from threading import Thread

#--------------Assets------------------#
base_path = os.getcwd() # root of repo eg. /software/ since main.py calls process

battery_sprite_path = base_path + "/menu/menu-sprites/battery_25_15.jpg"
folder_sprite_path = base_path + "/menu/menu-sprites/folder_21_18.jpg"
gear_sprite_path = base_path + "/menu/menu-sprites/gear_23_20.jpg"

small_font = ImageFont.truetype(base_path + "/display/alt-font.ttc", 13)
large_font = ImageFont.truetype(base_path + "/display/alt-font.ttc", 16)

class Display:
  def __init__(self, pi_ver, utils, main):
    self.main = main
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
  
  def draw_text(self, text):
    image = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(image)
    font = large_font

    draw.text((0, 96), text, fill = "WHITE", font = font)

    Display_Image(image)

  def get_settings_img(self):
    image = Image.new("RGB", (128, 128), "BLACK")
    draw = ImageDraw.Draw(image)

    draw.line([(0, 0), (128, 0)], fill = "WHITE", width = 40)
    draw.text((5, 0), "Settings", fill = "BLACK", font = large_font)
    draw.text((5, 26), "Telemetry", fill = "WHITE", font = large_font)

    return image
  
  def render_settings(self):
    image = self.get_settings_img()

    Display_Image(image)

  def draw_active_telemetry(self):
    image = self.get_settings_img()
    draw = ImageDraw.Draw(image)

    draw.line([(0, 26), (0, 42)], fill = "MAGENTA", width = 2)

    Display_Image(image)

  def render_live_telemetry(self):
    while (self.main.menu.active_menu_item == "Telemetry"):
      image = Image.new("RGB", (128, 128), "BLACK")
      draw = ImageDraw.Draw(image)

      accel = self.main.imu.accel
      gyro = self.main.imu.gyro

      draw.line([(0, 0), (128, 0)], fill = "WHITE", width = 40)
      draw.text((5, 0), "Raw Telemetry", fill = "BLACK", font = large_font)
      draw.text((5, 26), "accel x: " + str(accel[0])[0:8], fill = "WHITE", font = small_font)
      draw.text((5, 36), "accel y: " + str(accel[1])[0:8], fill = "WHITE", font = small_font)
      draw.text((5, 46), "accel z: " + str(accel[2])[0:8], fill = "WHITE", font = small_font)
      draw.text((5, 56), "gyro x: " + str(gyro[0])[0:8], fill = "WHITE", font = small_font)
      draw.text((5, 66), "gyro y: " + str(gyro[1])[0:8], fill = "WHITE", font = small_font)
      draw.text((5, 76), "gyro z: " + str(gyro[2])[0:8], fill = "WHITE", font = small_font)

      Display_Image(image)
    
  # special page, it is not static
  # has active loop to display data
  def render_telemetry_page(self):
    # this is not good, brought in main context into display to pull imu values
    Thread(target=self.render_live_telemetry()).start()