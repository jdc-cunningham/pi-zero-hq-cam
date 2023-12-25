class Menu:
  def __init__(self, display, camera):
    self.display = display
    self.camera = camera
    self.menu_mode = True # or False for camera
    self.active_menu_item = None
    self.menu_x = 0 # -1, 0, 1
    self.menu_y = 0 # -2, -1, 0, 1 (-2 is towards top)

  def update_state(self, button_pressed):
    if (button_pressed == "LEFT" and self.menu_x > -1):
      self.menu_x -= 1

    if (button_pressed == "RIGHT" and self.menu_x < 1):
      self.menu_x += 1
    
    if (button_pressed == "UP" and self.menu_y > -2):
      self.menu_y -= 1

    if (button_pressed == "DOWN" and self.menu_y < 1):
      self.menu_y += 1
    
    self.update_menu()
  
  def update_menu(self):
    if (self.menu_x == 0 and self.menu_y == 0):
      self.display.draw_active_icon("Files")

    if (self.menu_x == -1 and self.menu_y == 0):
      self.display.draw_active_icon("Camera Settings")

    if (self.menu_y == -1 or self.menu_y == -2):
      self.display.draw_active_icon("Photo Video Toggle")

    if (self.menu_x == 1 and self.menu_y == 0):
      self.display.draw_active_icon("Settings")