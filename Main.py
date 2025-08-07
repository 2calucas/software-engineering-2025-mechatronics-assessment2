#import microbit
# This code displays the current time in binary format on a micro:bit device.
# It updates every minute and shows the hour and minute separated by a colon.

#Hello Ryan if you are reading this, please help.

from microbit import *
import time

def to_binary(num):
    return bin(num)[2:]  # remove '0b' prefix

while True:
    t = time.localtime()
    hour = t[3]
    minute = t[4]
    
    # Convert to binary and format with colon
    binary_time = to_binary(hour) + ":" + to_binary(minute)
    
    # Scroll the binary time
    display.scroll(binary_time)
    
    # Pause for one minute before refreshing
    sleep(60000)
