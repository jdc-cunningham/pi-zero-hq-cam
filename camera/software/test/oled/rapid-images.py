# -*- coding:UTF-8 -*-

import io
import time
from picamera2 import Picamera2

#--------------Driver Library-----------------#
import RPi.GPIO as GPIO
import OLED_Driver as OLED

#--------------Image Library---------------#
from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

#----------------------MAIN-------------------------#

def Display_Picture(File_Name):
  image = Image.open(File_Name)
  OLED.Display_Image(image)

try:
  def main():
    #-------------OLED Init------------#
    OLED.Device_Init()

    img_id = 0

    images = ["picture1.jpg", "picture2.jpg", "picture3.jpg"]

    while True:
      Display_Picture(images[img_id])

      if (len(images) < 2):
        img_id += 1
      else:
          img_id = 0

  main()

# except Exception as e:
except:
    # print(e)
    print("\r\nEnd")
    OLED.Clear_Screen()
    GPIO.cleanup()

