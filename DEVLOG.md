12/09/2023

12:47 AM

I'm modeling the parts right now so I can arrange them in 3D space/get an idea of how big the body will be.

I am looking forward go going to the park when this is built and trying it out.

I haven't been to the park in idk 4 months looks like.

1:32 AM

Oh man, Metallica Slither, reconnecting with my roots.

I have 3D models of each part at this point, doing some alignment/initial body layout

It is useful to leave the Pi Zero usb/hdmi ports accessbile in case SSH isn't possible, can still get into it and modify code

2:02 AM

I think I'm going to have to build some of the hardware first (solder) to get a better idea of size/where things will be.

I think it's going to be a 2-board design

I will have to:

- solder male headers onto pi zero
- update pi zero w model to include male headers
- solder female header to skinny proto pcb board
- wire out the buttons/power distribution

Man... I don't really feel like soldering right now

I do need an LD33V and some size resistor not sure what I used on the ML Hat Cam, it's a 10K Ohm

2:24 AM

hmm... yeah I think I'll wait to do the soldering/electronics until I have some sleep/fresh mind

I can still do more rough designing of where things will go

the camera board will screw into the front case

pi zero w will be floating, other than being aligned by the ports/sd card slots, it's held in place by the GPIO connection

2:29 AM

I am still awake, I just don't want to attempt soldering right now, so I'll work on the software part

the main concern I had is if this idea of mine where I would have a semi-real-time image preview/zoom crop and display on the slow refresh OLED, to see if it was in focus

I can start designing the software though, even without the wiring

The d-pad will have to get screwed into the back case, since it gets pushed, OLED will be too just so it's under the case/flush

4:29 PM

Oh man... I just had an idea that will make this project even harder... add an IMU to it, for the horizon

The thing about this project is the OLED is the flaw... it is not bright enough in the sun/outside. So that makes the project kind of worthless but... it's a cool challenge to make/build a system (the hardware/menu).

I will solder the male headers first and make a basic power board with an LD33V to power the OLED because I need to get SPI to work... the waveshare library is too slow specifically the repaint. On Amazon I have seen someone playing a video/fast frame rate, that's what I need for this project.

4:54 PM

ugh man I'm feeling lazy... soldering is so nasty with my setup, this flux gets on my hands

I'm looking at this library, it's different than what I used for the ml hat cam

Damn... I did buy 2 OLEDs at some point... I gutted the ml hat cam for its OLED nooooo

ahh well... that project was gonna evolve anyway

the problem is I'm so disorganized, I have parts scattered all over the floor, have to look at my Amazon order history to figure out what I own.

5:15 PM

oh man my neck, I just soldered a 40 pin header to the RPi

inhaled more of that cancer smoke #living

okay, going to test that OLED library now

5:23 PM

Pi local IP 160

the IMU thing like using it isn't a problem, my concern is overlaying an image... which I can do that with OpenCV... but speed... is the issue.

what I'm going to test is the refresh rate with this library

I'm not sure how I'll have a camera display and seperate "take photo" if the camera is in use... will be interesting.

5:28 PM

slowed down by updating rpi zero, have to put git on it too and write code between deskop/pi to test hardware

5:34 PM

oh man this is taking a while, I just ran `sudo apt upgrade`

43% lol

I'll do most of the hardware soldering today... I was thinking I should use the bottom pins under the USB for power but it is also more convenient to power the Pi via its 5V GPIO pin... so there is just the female/male header connection that wires everything together.

There is a primary proto board and daughter board (shutter) but yeah.

the IMU will be using i2c so no pin worry, then just find 7 GPIO pins for the buttons

5:41 PM

99%

5:46 PM

ugh... I should not have looked/been reminded of my future that factory misery oh well I did it to myself

5:51 PM

alright pushing up then working through pi zero ssh for a bit

6:05 PM

ugh... there's a path problem

6:15 PM

god... why am I stuck on such a dumb thing "cAn'T fInD tHe FoLdEr"

6:23 PM

ugh... this is a weirdly named error message but I also can't read debug lines I guess

when trying to open SPI via `spi.open(0,0)` it says the "no such file or directory" which is misleading

https://forums.raspberrypi.com/viewtopic.php?t=154317

it runs now but nothing displayed

I have to verify the pins mapped in `OLED_Driver.py`

6:37 PM it's working, had a pin in the wrong spot, after updating the mapping in the driver file

Oh yeah the point of doing the OLED testing was more than just get it to work, wanted to see the refresh rate

the refresh rate is decent, the problem is it repaints the line top to bottom visibly...

it's probably wrong to use image display for a video stream

ugh man... it's probably a hardware thing you know, it's not a high quality display made for HDMI so it's slow

I see the nested loop iterating over each pixel and yeah... it's probably just how fast it can write data

I will try shifting an image around and see what that might look like

6:48 PM

oh man... my Sony A7 2 took a 6000x4000 image lol... scaling that down to 500x500 and then cropping 128x128 against it

7:00 PM

I think it is possible to make the refresh rate even faster but for now I need to build this thing

doing more soldering

7:18 PM

omg... I just thought of something stupid, it's like "why does it have an IMU in it? slow oled, slow img overlay..."

It can be a pedometer! omg... doesn't make sense, carry it in your hand, but that could be neat

thinking magnetometer but nah... not worth it, just use the 6 axis

7:22 PM

I'm getting dimensions now of how big the case will be, where stuff is, this way I can size the boards/start soldering those/doing the wiring

7:39 PM

Damn... this thing is not ergonomic at all, I'm trying to avoid sharp edges at least

8:01 PM

food break

I will have to make the two halves of the body nearly equal, bias with the front being shallow so I can get a screw driver in there to mount the shutter board... I'm thinking I'll just have connecting/sliding plates, orthogonal and then screws go into those to hold the thing together vs. deep screw holes or a deep body/back cover plate.

8:14 PM back on

man. I'm losing the drive, but gotta keep going

9:36 PM

did the wiring diagram, it's not 100% but shows where things should go

9:43 PM

I'm kind of lost right now, there's so much to do still but it's not hard

I need the body... but I also want to solder everything and program...



---

12/08/2023

10:25 PM

I wish I could say I was super excited/actively pursuing this. Right now the main thing on my mind is avoiding being homeless ha since I am unemployed/waiting to get my background check to work at amazon warehouse. This is all my own doing, I had a great job/quit, got another job slightly worse and that also didn't work out.

Anyway this is a project that I've had on my mind for a while/had the parts for but didn't get around to making.

I haven't worked on a hardware project since about 6 months ago. My most recent in-office job plus driving took about 11 hours of my day away every M-F.

I'm gonna get this done because it's a big project (lots of things to do) but I can still get it done in a few days. I'll just get lost it in for now.

I will also note yesterday I tried to reset my sleep pattern and I didn't finish it eg. slept at 9AM and woke up 6PM... so I'm kind of out of it.
