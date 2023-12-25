import time

from threading import Thread
from picamera2 import Picamera2

class Camera:
  def __init__(self, display, main):
    self.manual_mode = False
    print('stuff')