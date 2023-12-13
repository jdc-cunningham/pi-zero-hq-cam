12/13/2023

9:10 AM

- boot
  show splash screen
  start main.py
- 

12/12/2023

6:57 AM

Okay it's assembled at this point, sitting on my desk powered on, nice

I have an idea of how this thing will work

the live camera pass through consumes a lot of current 550mA is an average

so that will not be on all the time

I think this thing will be like a Tomogachi/companion and a camera

It has an IMU so it can sense motion

there is no audio/light feedback though unfortunately except the OLED itself

I have done audio out with a pi zero but it requires a lot of parts, it wasn't worth it to me for a shutter sound

okay I need to hit goals... once it's late enough eg. 9 AM I'll design/print the lense barrel clamps

9:13 AM

I designed the barrel wrappers for the 35mm lens (main), not sure if I'll do the others today, each one is different and the printing is 2-4 hours per piece, 2 per lens

---

12/09/2023

3:38 AM

Trying to imagine how this will work

- boot, start `main.py` loop
- camera shutter press would trigger photo (fast signal kill type)
- back button
  - opens menu if nothing is active
  - d-pad to navigate, go in, back button to go up layer
- menu system
  - view files
  - bluetooth pair
    - shows transfer option
- d-pad center
  - zoom (magnify, show top-left quadrant)
    - can zoom more, pan
  - pan around
