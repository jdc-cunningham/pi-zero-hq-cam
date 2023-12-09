12/08/2023

10:25 PM

I wish I could say I was super excited/actively pursuing this. Right now the main thing on my mind is avoiding being homeless ha since I am unemployed/waiting to get my background check to work at amazon warehouse. This is all my own doing, I had a great job/quit, got another job slightly worse and that also didn't work out.

Anyway this is a project that I've had on my mind for a while/had the parts for but didn't get around to making.

I haven't worked on a hardware project since about 6 months ago. My most recent in-office job plus driving took about 11 hours of my day away every M-F.

I'm gonna get this done because it's a big project (lots of things to do) but I can still get it done in a few days. I'll just get lost it in for now.

I will also note yesterday I tried to reset my sleep pattern and I didn't finish it eg. slept at 9AM and woke up 6PM... so I'm kind of out of it.

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
