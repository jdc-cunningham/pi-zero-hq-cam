underline for menu icon active is fine, top also looks tacky

astro mode also with photography

just point it at the sky

maybe assistive focusing via phone

12/24/2023

10:49 AM

Let's goooo baby, early day, thought I'd have to work till 5:30 PM like the usual

last night was bad man, my finger tip hurt so bad had to take ibuprofen to sleep

I took one in the morning too in order to get through the morning part of the day

thankfully I can type

the camera has a crop factor of 5.5 apparently so the 5mm is equivalent to 27.5mm so my thought of 35mm wasn't far oof, same for 12mm being like a 100mm full frame

so... I'm not 100% like if I let myself sleep in... still kinda in work mode since my mind was comitted to working that 10 hour shift

also got up 4.5 hours ago

let's get to it

10:59 AM

There's so much to it I feel overwhelmed, I know that it needs to:

- interactive menu
- zoom-pan-crop
- record video

At minimum for the next video/major progress of this project

But I want the other stuff to work too, battery status... IMU is being watched

Had a thought today about the threads needing to use callbacks so I don't have overlapping events, particularly with the display

11:01 AM

quick break

11:32 AM

Damn I'm tired

I have to mentally wrap this project up on this break (3 days off in a row) because after that I have to start applying for tech jobs

Concrete goals:

- camera turns on
- shows splash screen
  - current is a static image
  - [ ] future will be an animated chibi eyes character
- show the menu
- [ ] underline for active, none at first, camera ready message
  - need positions of each cursor, track previous to undo
- [ ] clicking center button (if camera preview not active) will open files... (center option) but not clear that's active
  - bring up cursor under files icon
- [ ] clicking arrows (left/right) moves cursor left/right
- [ ] up/down arrow allows you to go the upper row (camera toggle only) which can flip modes eg. photo or video
- [ ] boot
  - get battery status
  - bring up sensor(s)
- [ ] telemetry page
  - show the battery
  - cpu info
  - imu values (just accel 3-axis)
- [ ] settings page


That's plenty there to guide what needs to be done

---

12/23/2023

8:15 PM

I'm super tired today, my fingers/hands hurt

I binge ate so I'm in a food coma

I wanted to note that I thought about having video/part of the next video that focuses on the camera UI/UX and footage

Anyway I need a video mode/icon to toggle between photo/video

Won't have audio but gotta have that cliche focus pull

---

12/22/2023

5:57 PM

I will write code today, I don't want to wait for the 3 days off I have from work

Won't be crazy progress but something

6:11 PM

damn I'm spent... will try

6:28 PM

There is a "system design" thing I still haven't seen/figured out yet

I have to make the pieces to see the bigger picture

6:35 PM

I'm glad for the Pi Zero 2 upgrade, it's snappy, easier to develop on

6:48 PM

Ooh... not even that far already having separation of concerns issues

7:11 PM

man I'm so tired... my eyes hurt lol

Trying to draw a box on an existing image, the other examples were on a basic black background

7:43 PM

Ugh... I need primitives, it's not dry

Also need to separate state from display logic eg. the menu vs. display code

7:44 PM

Ooh... I just had an idea... it could get annoying but when you point the camera at the ground, this chibi animation could briefly popup (blinking eyes)

That feature (blinking chibi animation) is on my list of things to do but for now just using that generated character

Damn I'm so tired... what I need to do is make this code simpler/reusable and then be able to pass in a flag (currently duplicated code) eg. if it's making a menu inactive it just flips the color of the line fill

The telemetry will show the IMU live readouts and details about the pi zero 1/2 eg. cores/ram/storage/etc... just data (excuse to show something cool)

the IMU thing I want the horizon level (it would go over a photo)

7:50 PM

I like the way react works, where you pass in parameters and it outputs a display

I'm thinking about doing that with the menu, will see

8:03 PM

Oh I forgot, I had an idea for an expansion USB mic/speaker it's like a T-shape (center speaker, strereo mic)

That would be an easy way to add that feature, but it's a custom chip design, outside my skill set right now

---

12/21/2023

7:16 PM

Tired af... have a headache

Printing the remaing lens parts... trying to do something for the menu

I had thought about having indidivual sprites that are stacked on top of the base image, this would make updates easier but you have to repaint them/stack in a row vs. paint 1 image once

7:44 PM

I'm not sure if this was a dream but while I was trying to/in the process of sleeping I thought about checking the variation/contrast from one pixel to the next (frame draw) and if it's not too drastic, keep it so only the new pixels get updated, this would be for the (desired) high FPS live preview.

This is so dumb it's hand drawn but it's not about the scenes (can be updated), just working on the flow.

I was also thinking for recording, red dot, side note no audio sucks, but also one less thing to worry about

11:05 PM

what the heck man... this lens cap is still too small, I'll have to do it again tomorrow, at least it's an hour print but still... this'll be the 3rd attempt

---

12/19/2023

2:16 PM

Feel slow today... printing stuff

Supposed to be designing the menu

2:56 AM

Still no motivation yet, maybe feeling something

4:00 PM

oh no... I measured wrong on the 35mm I measured including the base ring damn...

since it's printed orthogonal long ways, I was able to just slice off the excess.

I'll fix the design

