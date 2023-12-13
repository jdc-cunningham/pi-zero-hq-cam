12/13/2023

8:53 AM

It's a new dawn... it's a new day

Going to write the bare mnimimal functional code to use this at the park

Man it's a gloomy grey day outside not a good day for photos oh well, I'll still get out there

9:00 AM

omg... I just screwed up my Chrome user profile... I accidentally hit "sign out" on YouTube and it signed me out of all my Google Accounts... wtf.

A problem for another time

Alright I think I'm coming around with the barrel lens thing, it does make it more legit than the tiny lens

10:25 AM

quick break

10:57 AM

eating some food, I have the charger plugged in while the camera is on... kind of cool

keep it topped off

ugh... hate when an OS resumes wtih multiple monitors and windows shift around, happens in both windows and mac

11:02 AM

waiting for my ramen to cook (reduces my lifespan)

I was thinking about the menu system, how you can individually repaint stuff like an icon in a corner, that would make for a more "real time" UI

11:23 AM

back on

11:53 AM

oh no... I forgot about a GPIO being affected by the camera being on

nooooo please, I don't want to take this thing apart

oh no... this is odd though, GPIO 1 is the one that affects the camera

but the buttons show LEFT (being printed/active without being pressed) which is 17

11:57 AM

I disabled the camera and I'm still seeing left huh

could it be a short? why now

try reboot

dang shutter is bound to GPIO 1

I'll use the test button code to see

no short

I wonder if it's from the OLED

12:10 PM

it's odd... it's just stuck in on

I tried setting the GPIO to low

12:14 PM

Hmm... seems like if I clear the GPIO pins (end of OLED test) buttons are fine again

12:18 PM

hopefully this does not mean there is a conflict when OLED can be on/when buttons can listen

12:26 PM

hmm... still having a conflict

12:29 PM

oh man........ I've been trying... but maybe the easiest solution is to not use this pin

since all the other pins are fine

okay... I'll do it

I'll use GPIO 21, it's random/far away from stuff, by ground

12:43 PM

soldered

I'll verify if GPIO 1 is affected by the camera or not

While I have it taken apart

12:48 PM

live preview not working, did it take a photo?

no

12:57 PM

ooh I didn't start the camera... now we'll see if GPIO 1 is a problem

1:07 PM

oh no... back button looks like it's affected by the camera what pin is that

GPIO 7

Alright I'll just move it... to 20 right next to the left button

1:37 PM

hmm... the code is not working well in a thread, not sure why

1:41 PM

no... please tell me my OLED did not die

I'm hoping it's just low on battery

Damn the charger melted the hot glue

On the plus side the sun came out...

It must be very low on power to get this hot

1:58 PM

Oh man that scared me... it's working

The charging board is sus though, I wish it had a screw/mounting block, since it reheats the hot glue and detaches itself from the plastic... I added a double sided-foam tape but it's only one one side since the body splits in half

I'll add theo ther half and when the body comes together hopefully that'll help shear

I'm going to put it back together

2:10 PM

charging, need to continue writing some code, very basic text

so far the photos are not good, need to be able to focus/compare

2:15 PM

Alright I'll keep going, then charge before I leave for the park

Damn... I have to wait for it to charge.

When the OLED starts to paint and then camera starts, the OLED dies

hmm.... running low on time, have like 2 hours at best

I need to drop the minimum code, what I'm missing is a file counter

To tell me photos are being taken

2:43 PM

done charging, I'm hoping it's not like the camera + oled + pi is too much current that would be bad... shouldn't be, it's a 2A boost converter... worst case I use the higher paying one but then I'd be concerned about the battery

I think if you use a 2S battery it uses lower current but I don't have a charger/bms thing for 2s

2:46 PM

interesting when you take a photo the OLED refresh thing fails to work

makes sense to stop/pause it while taking a photo

2:50 PM

soon as I try to take a photo the OLED update goes bad, still keeps going though

okay... it is a stale variable reference issue

3:03 PM

there is a debounce problem with the button

I have to not accept input until I'm done with the first event

oh no... I never did a current draw for when the camera is active and oled showing

I'll just assume it's even worse/bad

the timer is not working

3:14 PM

hmm... I'm not sure if it's code or a power issue

I have to leave soon for the park

I think it's code... not being completed before starting something else

3:21 PM

One thing is, I need to stop the camera when the preview isn't active

I'll also use pause instead of stop

I'm missing two things bare minimum:

- boot entry
- file counter, this can display on boot

---

12/12/2023

4:26 AM

dang... up 32 hrs, only slept for 4 hrs, today will be rough but I'll follow the plan (reset sleep pattern) I think it was the salt that woke me up (ate ramen meal)

on boot the camera jumps around 220mA is an average current draw

then idling with no OLED on its around 170mA

these are more biased to a higher value

I will turn the OLED on solid white I think that is the highest draw, this will be a good avg value for when the oled is just drawing stuff

ssh active it's hovering around 200mah

the software battery tracking I was thinking when it does some power intensive thing it will reduce the theoretical lifetime

solid white spiked 400mA, 341 mA active

black square is normal, off I guess makes sense

so I think if it's a menu imag I can expect 275mA or 300mA as an average current draw

4:37 AM

two videos: hardware, software

need to have the lens wrappers designed/printed first for all 3 lenses and shot at the park

example photos taken by cam

5:16 AM

I forgot the hole for the switch dang

5:53 AM

OMG it's assembled, 6.3oz weight no lens

6:19 AM

a little distracted, just charged up the battery

planning the menu out/process logic

I want to actually use it take pictures but I need those rotating rings

6:23 AM

oh right I gotta test that everything still works after being assembled

I wish it had sound/led's or something, for indicators, I guess I'll just use the OLED, for the photo for example, I figured I'd flash the OLED white when it took a photo

6:50 AM

I didn't track when I turned the camera on, now it's time to write some code

I had some basic plan on what I'll be doing

7:08 AM

quick food break

7:41 AM

I'm gonna start designing/printing those barrell rings, I shouldn't (use fresh mind on code)

But I'd like to print those while I'm writing code

7:54 ehh... I'm just going to use glue

I was thinking of screw holes but they might be deep, don't want to deal with cutting/testing

hot glue will come off easily when wanted from metal

8:00 AM

ugh... I don't want to do it, to design the barrell parallel line grips

damn it... I'll do the screw clamp

8:03 AM

I'll do it... the vertical line grip things... it'll look better, contrast the otherwise smooth body

8:36 AM

dang... it's a 2.5 hour print for 1 piece

8:53 AM

I won't design the other ones now, I'll just use them as is no outer ring

Alright I got into the zone/bust this code out

I think the gap I cut out is not enough/needs to be more so it squeezes more.

Did have a thought, you could have a lens hood design

9:22 AM

Dang I feel tired, not sure how well I'll do with writing code today

Today might be a wasted day (stay up late enough then sleep)

Yeah... I think I'll work on the media stuf right now (YouTube videos/blog post)

11:01 AM

alright just printed... it's a little loose, I'll add back in the standard clearnace 0.01 that I take out.

it's not unusable so I'll print the other part 4 hrs

Dang... I think it'll look more legit if the end is closed

I'm just going to keep it loose, it's easy to fix with some tape

1:03 PM

I'm unfortunately mentally spent, tired mostly, I'll get basic code written tomorrow where camera is usable in the wild, will skip battery part

3:54 PM

rings were printed... they are a bit loose, if you put tape in there to shim it, it makes them not sit straight

the screwdriver hole needs to be larger too

4:41 PM

ugh... I tried increasing the gap on the focus ring but surface issues, oh well I'm past it

I made the ring contact area have a higher tolerance

I'm done today, I want to write the code but I'm spent

lens cap won't fit over barrel lens, it could but then you have to fish it out between the gap

---

12/11/2023

12:03 AM

I need to do a battery capacity usage check, before it becomes assembled

I'll do this while writing some software

I'm gonna take a quick mental break (watch tv) today will be a long long day ha... if I make it.

My reward will be real food vs. pb&j

12:12 AM

I'm going to add a JST connector the battery so it's easy to swap it out if it dies, dies as in not rechargeable

On at 12:18 AM, blue full charge

Will run it for 1 hour

It's just on though, camera is plugged in but not streaming

12:43 AM

I bet there is a way to make a menu renderer in python

as in it's like react where it's functional, you feed it states, renders... without the OLED

- boots
  - ask if charged (battery)
  - show camera pass through, wait for buttons, maybe overlay telemetry/horizon,
    sample imu in separate thread
  - shutter (photo)
  - button (show/navigate menu)
  - CRON sqlite db counter for battery consumption

12:58 AM

I'm borrowing code from my ML Hat Cam project which was also a camera with a menu interface

1:12 AM

Ooh fun the menu can be a set of sprites then you move a square around the active one

This is cool it's like a little OS UI (thinking of a watch)

Oh man... you can add a scroller too...

omg... a file system yo... I mean it enumerates the files but then generates tiles based on file count damn...

yeah some menu system exists out there for oleds but it's fun to make your own/figure out how

coming up on the time to check 1 hour of battery consumption, need to do some minor soldering

I really wish the camera was assembled already but I can still do software work without being assembled

1:25 AM

Ugh... this test will not be accurate, I accidentally touched the pos/neg ends of the lipo together while desoldering from the charger reeeee

1:32 AM

oh man I'm excited... I just had an idea since I can put images on the menu/display I can be a weeb hahahaha

actually not an original idea I was inspired by this Osaka OS project I saw on YouTube

wow it only used 60 something mA for that hour it was on... I guess it makes sense it wasn't doing anything

yeah says 65mA while idling dang

1:52 AM

lmao it is done, picked something from waifu labs

I have to test some menu displays with the OLED, I've used it before but this library is different

Have to see what primitives are there to work with

2:06 AM

I'm having trouble starting, so many things to do... I really wish the camera was in 1 piece

the camera pass through thing is hard, the pieces are easy-ish

actually I think the web stream may work since it produces a buffer and then you directly write it to the OLED display

so you have that as a thread, always running then you can tap into it from the main process

I do have to do some agressive scaling to show it on a 128 display

4056x3040 oh yeah then to "take a picture" you don't discard the active image

2:16 AM

this battery discharge is distracting me, I'm waiting for it to do its annoying beep

2:30 AM

Alright fully present, 3.5 hrs before I gotta do shopping and then start 3D printing

I gotta stay up 2 days in a row to flip my sleep pattern hopefully this time I commit, I should will have food

2:34 AM

doing some reading here

https://raspberrypi.stackexchange.com/questions/58871/pi-camera-v2-fast-full-sensor-capture-mode-with-downsampling

I want to first check what size image I can get

2:41 AM

reeeeee I decided to rename the repo to a shorter more generic name

getting tired of cd'ing into the directories in ssh

2:47 AM

oh damn this could work

https://github.com/raspberrypi/picamera2/blob/main/examples/capture_to_buffer.py

maybe

3:08 AM

dang it I'm close... I need to make the buffer into an iterable array

3:15 AM

omg... I wrote something to the camera nice

3:21 AM

I'm trying to figure out why my photo is a crop not scaled down

3:22 AM

I still have the issue of not using buffers directly, still juggling PIL

3:29 AM

I am wondering if it's inevitable to use a video stream, it has the high and lores (lores goes to oled)

When you zoom that config has to change on the fly

Or resize the image...

crop info

https://github.com/raspberrypi/picamera2/issues/498

3:39 AM

Omg finally I got it... let's see how fast it can go

3:41 AM

ha... idea, IMU moves around the character on OLED moves with it

3:54 AM

Let me do a quick time check to see where the slowness is

it's the iteration that's slow

4:21 AM

I'm going to try solid color patterns

I'm still screwing around with framerate

4:24 PM

it's the same, visible update

4:28 AM

anyway the PIL/buffer part isn't slow, it's the writing data/SPI

it takes about 60-70ms per frame

which is around 15fps

5:23 AM

I was wrong above, each frame takes around 600ms+ so it's 1.5fps damn

I want to believe it can be optimized... but I'm not sure if it can be done in C or what...

I messed aroudn with the SPI speed, not any significant change

Tried to figure out how to make an 8bit image, didn't get far on that

5:31 AM

I'm going to have to move on from this for now, it's something that can be improved in the future

5:37 AM

Not bad progress though I mean I was able to make the passthrough despite it being slow af

I'll continue later/start printing, gotta do a grocery run

6:39 AM

it's pitch black outside right now, waiting a little more before I go

I was thinking. for the menu, I can do an image paint, then draw the square on its own around the active menu/unpaint the previous (need to track) state

I should be able to fully build this thing today... a couple hours test prints then 13hrs for both parts

I'm thinking of this arches look for the lens barrel wrappers hmm may look bad

6:46 AM

Ugh... I don't want to wait anymore... soon this will be the time that I work anyway

7:52 AM

let's goooo babyyyy man has provisions

Also let's start printing

8:08 AM

So I'm gonna be homeless in like a month but right now I have food, I don't have a job, I don't have anywhere to be, I'm free!!!... for a bit lol. I'm psyched

8:55 AM

test prints are good, almost ready to do full prints

will low-key design the menu interfaces while I binge eat/watch tv to stay up

9:08 AM

Camera test fit is good... do I full send... or test the gaps...

Full send baby GODDDDDD 8 hrs bro... it's 9 it won't be done till 5 damnnnnnn

is that how time works?

11:57 AM

Damn... I'm so tired I can't even watch tv, I can't pay attention

5:10 PM

first print is done

also my fate is sealed at the warehouse, will be starting in 3 days RIP

6:11 PM

so spent... just waiting for the print, will assemble and program tomorrow, will get the lens rings done too, would be nice to take it out but I want the full effect... sadly Wednesday is cloudy

First thing I'll do tomorrow after assembly is to program it, fresh brain

6:17 PM

I was screwing around with the lens and I was able to free/unlock the zoom on the 12mm, I'll try to do the same on 5mm, guess it was just stuck/turned too much in one way.

6:18 PM

heck yeah it's unfrozen, nice

7:32 PM

doing some light thinking

I've been up 28 hrs so far. 32 hrs baby, then I sleep, hopefully don't overshoot my wake up time

9:05 PM

ladies and gentlemen I had a thought... get a current draw measurement while it's doing the camera loop/paint

dayum! it draws 546mA holy crap...

damn I'm bad at math... this thing won't last 2 hours

9:15 PM

okay... what this means for now is... the passthrough won't run all the time

and I will also get a larger 1S pack, there is plenty of room

10:42 PM

omg it fits so well... I'm tempted to assembled but I need to sleep

tomorrow

---

12/10/2023

1:56 AM

At this point I've gotten a lot of the soldering done, I accidentally mirrored the OLED pins on the RPi GPIO at least they were just digital pins/not live ones eg. 5V or ground.

I still have to finish soldering the buttons and test them

Then update the design with regard to the hardware change and final dimensions

The wiring is nasty unfortunately since the wires I'm using are thick and not grouped together like those ribbon cables that are joined

Okay I'll work on soldering the buttons to the board, it's not a huge deal but would be nice to verify those are functioning/bind them in a python loop

2:24 AM

oof... I just had a thought, if I'm not using a video stream/buffer directly to OLED then this thing will be even worse/slower than these 3 sample images because the images have to be generated before displaying so it'll be even slower, damn.

3:08 AM

AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH I did not give the dpad much slack so it is far away from the OLED

this means... I can fit an 18650 cell... means the design will have to change again...

the only reason I don't want the 18650 cell is it needs a case... otherwise it is an ideal form factor

No I won't do it

ugh man... it will just be a block, I'm losing drive to make this thing fancy because I gotta go back to reality soon

3:53 AM

Dang... I'm spent... I've got the base dimensions down just based on the wiring/volume.

I'm aligning stuff/doing the screw holes now

ugh it's ugly af... too round (corners)

5:07 PM been working on this since 4PM I'd say

5:48 PM

making progress just designing, getting close to printing again, unfortunately it's night time so I can't really print much

6:41 PM

the charger turns blue when it's done

I'm again running into the dumb problems sketchup has, I think it has a memory leak (leave it on long enough it gets slow as hell) the other issue is the surfaces... oh well, learn a real CAD program

I will print parts of the body invididually to check clearance before printing the full thing

8:25 PM

ugh... I'm wondering if I should use a 9-axis IMU for true dead reckoning... maybe it's overkill. It's not too late.

It's good enough... but.... I'll do it... they're the same form factor so it's just some soldering.

issue now is I have to find a raspberry pi library to interface with this thing, it does not seem to be the same as an MPU9250

I could just try it though...

8:51 PM

it still works wow... cool that'll work then.

I have written dead reckoning code before not sure if I need it but it's in python/based on some matlab guide

wow these things are not cheap $10 each

10:39 PM

alright... I have the two halves, now need to design some way to join them together by a few screws

I really wish I could print, will have to wait till tomorrow

---

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

ehh.... I think I'll put the JST plugs for the batteries on top of the camera in channels, then you just tape over them with black electrical tape to blend in... ugly but I don't want to make some hinge mechanism or deal with a balancing charger for two parallel cells

11:22 PM

decided to change battery to 2S series, 800mAh it's smaller capacity but easier with regard to wiring/charging run time will be 3-4 hours (absoultely exhausted by 4).

means stepping down too vs. step up, bigger component

I have these 1100mAh packs but they seem puffy despite not being used...

Ugh... idk what to do. I have these USB charging boards, that would be nicer but it's 1 cell... largest 1S pack I have is the 720mAh set... so that's a run time just over 3 hours, but that's continous... I would think it's rare to keep a camera on that long.

turn it on to do your shots, turn it off to walk somewhere

Ugh... this cutoff voltage is too low for a lipo, it cuts off at 2.5V

oh man... alright just so it's more legit I'll use the charging board since that's prettier, USB in but it will still require a time-based battery check

---

12/08/2023

10:25 PM

I wish I could say I was super excited/actively pursuing this. Right now the main thing on my mind is avoiding being homeless ha since I am unemployed/waiting to get my background check to work at amazon warehouse. This is all my own doing, I had a great job/quit, got another job slightly worse and that also didn't work out.

Anyway this is a project that I've had on my mind for a while/had the parts for but didn't get around to making.

I haven't worked on a hardware project since about 6 months ago. My most recent in-office job plus driving took about 11 hours of my day away every M-F.

I'm gonna get this done because it's a big project (lots of things to do) but I can still get it done in a few days. I'll just get lost it in for now.

I will also note yesterday I tried to reset my sleep pattern and I didn't finish it eg. slept at 9AM and woke up 6PM... so I'm kind of out of it.
