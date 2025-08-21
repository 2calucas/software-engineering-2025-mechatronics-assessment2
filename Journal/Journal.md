
# Journal

Created on the 24/7/2025 





Ryan Hupp & Cal Lucas was teamed up to do a project 'Year 11 Software Engineering - Year 11 Assessment Task 2 - Mechatronic & Object-oriented Programming - Binary cloock with sound based alarm control'. This will a shared project, with two classes; Time to Binary and Controlled Sound Alarm.

>-------------------------------------------------------------
|

|

|

Date - 7/8/2025
-------
6:30 AM
Cal L
-------



Achievements
> I have added 2 imports including:
    > microbit |
    > utime |
> This will help me to add clock functions and detecting what time it is when adding an alarm system |

-------------------------------------------------------------

Problems
> I have one problem so far, this including: 
    > Local time - from the import 'time' |
> I do not know how to fix this as it is a browser based code editor |

-------------------------------------------------------------

Goals
> Get clock function working |
> Get Alarm system working |
    > Set Alarm |
    > Make Noise when alarm is timed |

>-------------------------------------------------------------

|

|

|

12:30 PM
Cal L 
-------

I import some modules: microbit, utime, and speech. The microbit module gives us access to the hardware, like the LED display and buttons. The utime module is key for anything time-related, and the speech module lets the micro:bit announce the time (This for testing use only). We kick things off by setting a starting time—just the hour and minute—so we know where we’re starting from. To keep track of how much time has passed, we record the starting time in milliseconds.

Next, we have a function that converts numbers into binary. This is super important for showing the time on the micro:bit’s LED matrix.

Now, the heart of the program is a loop that just keeps going. Here’s what happens inside:

It calculates how much time has passed since we started.
It updates the current hour and minute based on that elapsed time.
The speech module chimes in to announce the current time.
The current time gets printed to the serial console for debugging—because why not?
The time is displayed in binary on the micro:bit’s LED, scrolling across the screen with a colon in between.
Finally, it takes a one-minute break before starting the whole thing over.
This program shows off the micro:bit’s skills as a timekeeper, giving us both sound and light to keep us informed. It’s a pretty good and engaging way to use this little device.

-------------------------------------------------------------

Achievement 
>I have Got the clock to work |
> Time to Speech |

-------------------------------------------------------------

Problems
> NO alarm system implemented yet |
> No OOP implemented yet |

-------------------------------------------------------------
Goals
> Get the Alarm system running |
> Get it to apply with OOP |

>-------------------------------------------------------------
Date - 11/8/2025
-----
2:04 PM
Cal L & Ryan H
-----
Achievements
> Added alarm and started on OOP
> Removed Utime
> Added import music
> Added class binary clock
    This includes: hours, minutes, alarm hours, hours in alarm minutes.
    Def set_time
    Def set_alarm
    Def increment_time
    Def check_alarm
    Def time_to_binary
    Def scroll_time

Added class: Microbit Clock System
    Def manual_setup
    Def get_number_input
    Def run

-------------------------------------------------------------

Problems:
> The alarm system currently consists of a three second delay (but the minutes are alined perfectly)

-------------------------------------------------------------

Goals:
> Adding a reset button for alerm system

-------------------------------------------------------------

Description:
As of now, the project is coming along smoothly, and it will be handed in on the due date. The Code has evolved from traditional programming into OOP (Object Orientated Programming) meaning it will be optimised.
The big jump from traditional programming to OOP was difficult as Cal is not very professional in that particular field.

As for Ryan, he decided to wake the hell up and start contributing to the duo in the form of the journalist, documenting the process as time goes on. (Seems those writing skills were useful after all.)
-----------

Date - 18/8/2025
---
Cal L
---

Achievement:
> Created A schematic

> Finishing up on the README.md

Goals:
> Finish all work


Troubles

N/A

Description:

I have been working on the schemeatics, which Mr Saini helped me with (thankyou sir). The schematics contain 7 resistors, 6 LEDs, 1 speaker and 2 buttons that is to give a rough outline of what hardware that I am using.
I am also finishing up on the README.md File that will tell you how to use the program and how to read the schematic (roughly).
----

Date 21/08/2025 - 12:30pm
---
Cal L
---

Achievement:
> Added extra comments within the code for better explorations for the teacher

> Removed While True, because it was going to ruin the clock system