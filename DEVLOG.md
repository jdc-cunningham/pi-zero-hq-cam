- add timelapse feature (too easy not to do)
  - can timelapse the water line of lake
  - add t prefix to file name
  - need submenu to set interval time (minutes)
- add battery manager
- charge before going

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