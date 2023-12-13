12/13/2023

9:10 AM

- boot

  show splash screen

  start main.py

- idle state
- click center/shutter button, show live camera pass through
- zoom pan is hard, I need to think about it, I would like some form of zooming though for focus verification

  this might be extra
- count down 10 seconds if nothing happens disable
- shutter = take photo, show black/photo taken message (all white is too much current draw lol)
- first menu to see list of photos
- display?

There is unfortunately a lot of work to do still and I only have most of today to get something made

Oh menu lens select would be nice, since no way to tell what lens is used

I kinda wish I added a speaker... I would have had to make a little board with all the parts eg. capacitors then use Adafruit's speaker



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
