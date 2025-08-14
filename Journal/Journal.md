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



Acheivments
> I have added 2 imports including:
    > microbit |
    > utime |
> This will help me to add clock functions and detecting what time it is when adding an alarm system |

-------------------------------------------------------------

Problems
> I have one problem so far, this including: 
    > Local time - from the import 'time' |
> I do not know how to fic this as it is a browser based code editor |

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

Acheivment 
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
Achivements
> Added alerm and started on OOP
> Removed Utime
> Added import music
> Added class bynary clock
    This includes: Hours, minutes, alerm hours, hours in alerm minutes.
    Def set_time
    Def set_alerm
    Def increment_time
    Def check_alerm
    Def time_to_bynary
    Def scroll_time

Added class: Microbit Clock System
    Def manual_setup
    Def get_number_input
    Def run

-------------------------------------------------------------

Problems:
> The alerm system currently consists of a three second delay (but the minutes are allined perfectly)

-------------------------------------------------------------

Goals:
> Adding a reset button for alerm sysem

-------------------------------------------------------------

Description:
As of now, the project is coming along smoothly, and it will be handed in on the due date. The Code has evolved from traditional programming into OOP (Object oriantated Programming) meaning it will be obtimision friendly.
The big jump from traditional programming to OOP was difficult as Cal is not very proffesioned in that particular field.

As for Ryan, he decided to wake the hell up and start contrubuting to the duo in the form of the journalist, documenting the process as time goes on. (Seems those writing skills were useful after all.)