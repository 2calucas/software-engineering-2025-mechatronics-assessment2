# Journal

Created on the 24/7/2025 

Ryan Hupp & Cal Lucas was teamed up to do a project 'Year 11 Software Engineering - Year 11 Assessment Task 2 - Mechatronic & Object-oriented Programming - Binary cloock with sound based alarm control'. This will a shared project, with two classes; Time to Binary and Controlled Sound Alarm.

>-------------------------------------------------------------
|

|

|

Date - 7/8/2025
-------
6:30 am Cal L
-------



Acheivments
> I have added 2 imports including:
    > microbit |
    > utime |
> This will help me adding clock function and detecting what time it is when adding an alarm system |

-------------------------------------------------------------

Problems
> I have one problem though so far, this including: 
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

12:30
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