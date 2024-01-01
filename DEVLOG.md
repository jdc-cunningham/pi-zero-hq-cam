- add timelapse feature (too easy not to do)
  - can timelapse the water line of lake
- add battery manager
- charge before going

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