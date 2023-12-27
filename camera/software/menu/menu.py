class Menu:
  def __init__(self, display, camera, main):
    self.main = main
    self.display = display
    self.camera = camera
    self.menu_mode = True # or False for camera
    self.active_menu_item = None
    self.menu_x = 0 # -1, 0, 1
    self.menu_y = 0 # -2, -1, 0, 1 (-2 is towards top)
    self.menu_settings_y = 0 # I'm seeing the pattern now, grouping
    self.active_menu_item = None

  def update_state(self, button_pressed):
    if (self.main.active_menu == "Home"):
      if (button_pressed == "LEFT" and self.menu_x > -1):
        self.menu_x -= 1

      if (button_pressed == "RIGHT" and self.menu_x < 1):
        self.menu_x += 1
      
      if (button_pressed == "UP" and self.menu_y > -2):
        self.menu_y -= 1

      if (button_pressed == "DOWN" and self.menu_y < 1):
        self.menu_y += 1

    if (self.main.active_menu == "Settings"):
      if (button_pressed == "DOWN" and self.menu_settings_y < 1):
        self.menu_settings_y += 1
      
      if (button_pressed == "UP" and self.menu_settings_y > -1):
        self.menu_settings_y -= 1

      if (button_pressed == "BACK"):
        if (self.active_menu_item == "Telemetry"):
          self.active_menu_item = None

        self.menu_settings_y = 0
        self.display.start_menu()
        self.main.active_menu = "Home"

      if (button_pressed == "CENTER" and self.active_menu_item == "Telemetry"):
        self.display.render_telemetry_page()
        self.main.processing = False
        return

    self.update_menu(button_pressed)

  def update_menu(self, button):
    if (self.main.active_menu == "Home"):
      if (self.menu_x == 0 and self.menu_y == 0):
        self.display.draw_active_icon("Files")

      if (self.menu_x == -1 and self.menu_y == 0):
        self.display.draw_active_icon("Camera Settings")

      if (self.menu_y == -1 or self.menu_y == -2):
        self.display.draw_active_icon("Photo Video Toggle")

        if (button == "CENTER"):
          self.camera.change_mode("video")
          self.display.toggle_text("video") # what
        
        if (button == "BACK"):
          self.camera.change_mode("small")
          self.display.toggle_text("photo")

      if (self.menu_x == 1 and self.menu_y == 0):
        self.display.draw_active_icon("Settings")

        if (button == "CENTER"):
          self.display.render_settings()
          self.main.active_menu = "Settings"

    if (self.main.active_menu == "Settings"):
      if (self.menu_settings_y == 0):
        self.display.render_settings()
      
      if (self.menu_settings_y == 1):
        self.display.draw_active_telemetry()
        self.active_menu_item = "Telemetry"

    self.main.processing = False
