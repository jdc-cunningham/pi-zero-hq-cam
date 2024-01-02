- add timelapse feature (too easy not to do)
  - can timelapse the water line of lake
  - add t prefix to file name
  - need submenu to set interval time (minutes)
- add battery manager
- charge before going

01/02/2024

9:17 AM

Damn I feel slow today

I want to wrap this up and then return to my reality of trying to get a new job

9:23 AM

At some point I ought to make a tripod base mount thing... particularly when I actually start dialing in the colors/get better photos

That'll be near summer though, something worth photographing

My t-key is dying man damn... I've been using this durgod 65 hades for 3.5 years now

I've swapped switches around that died, it's not easy though have to desolder

the battery init is wrong, it keeps saying 3 hrs so I gotta dump that table and see

9:30 AM

Some noted bugs:

- frozen after photo (I think related to zoom in/out)
- after timelapse menu painting is messed up
- can't switch back from vid to photo
- timelapse doesn't stop after backing out

9:45 AM

Oh yeah CRON wasn't working right so battery wasn't decrementing

9:48 AM

Yeah timelapse stop isn't working, back doesn't stop it interesting



---

01/01/2024

10:02 AM

New Year New Me? Maybe

Slept in a bit, got ready... man my body is in pain... took an Ibuprofen

"Within my mind I'm everyone..." not sure my this SP song came to mind but yeah

So it's cloudy right now, should clear up in 3 hours, I'll write the battery profiler/timelapse feature by then

The timelapse won't be permanent code since I have to come up with a pattern for the muli-level menus and state management

10:12 AM

Ugh... my mind is already swimming

I think I decided to give myself 1 day out of the 3 days off to have fun... the rest of my time is trying to upskill/get a new job/freelance

10:26 AM

What's bad about the current menu system?

- lot of if else branches
- disconected between the two functions/no logical flow of state
- no order/structure, can't go past 1 depth since it's harder
- random state everywhere in menu properties

10:35 AM

ugh... my mind is all over the place

10:53 AM

Alright now to try this battery profiler code out

12:21 PM

Alright so the basic battery profiling interface and db/cron job has been setup

I need to add a quick timelapse mode then go to the park

It is unfortunately cold... 33F so I'm not sure how well this will go but it will be an adventure

12:32 PM

writing the timelapse code, it'll be short eg. take a photo every 60 seconds since I won't stick around for hours

I will shoot a brief timelapse of the shoreline, that would be something moving and perhaps capture overhead clouds moving

12:36 PM

The battery profiler still needs work, I need to manually trigger that question/make sure it works

6:42 PM

Editing a video, there were bugs... but nothing a power cycle couldn't fix lol (sad)

the timelapse does not stop/keeps going

the ordering of photos (based on epoch timestamp) is off for some reason... it's like it goes backwards in time on next boot

I still have some things to wrap up before merging this code so I'll do it tomorrow morning

---

12/31/2023

6:48 PM

damn... just finished my last day for this week's 4x10

I'm spent... but I was thinking about doing something for this project

I ordered a used RODES wireless 2 mouse... hopefully the sound is still good lol

I want to use that, but also I want to go to the park with the camera

But this devlog is about the battery profiler

was thinking

- every 5 minutes write to a file via CRON
- every other minute turn the live preview on, this would result in 50% camera usage
- from there should get some idea on hours
- need to setup sqlite3
- maybe use a config.json file for the battery life info

- profiler started by settings page
- when camera dies/recharged, the intro question (pick yes regarding charged) would reset stuff to 0
- pull 80% of max life