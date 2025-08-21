from microbit import *
import music

class BinaryClock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.alarm_hour = 0
        self.alarm_minute = 0

    def set_time(self, hours, minutes, seconds):
        """Set the clock time manually."""
        self.hours = hours % 24
        self.minutes = minutes % 60
        self.seconds = seconds % 60

    def set_alarm(self, hours, minutes):
        """Set the alarm time manually."""
        self.alarm_hour = hours % 24
        self.alarm_minute = minutes % 60

    def increment_time(self):
        """Simulate clock ticking every minute."""
        self.minutes += 1
        if self.seconds >= 60:
            self.seconds = 0
            if self.minutes >= 60:
                self.minutes = 0
                self.hours = (self.hours + 1) % 24

    def check_alarm(self):
        """Check if alarm should trigger."""
        return self.hours == self.alarm_hour and self.minutes == self.alarm_minute

    def time_to_binary_string(self):
        """Return the current time as a binary string."""
        h_binary = "{:05b}".format(self.hours)   # Hours: 0–23 needs 5 bits
        m_binary = "{:06b}".format(self.minutes) # Minutes: 0–59 needs 6 bits
        s_binary = "{:06b}".format(self.seconds) # Seconds: 0–59 needs 6 bits
        return h_binary + " " + m_binary + " " + s_binary

    def scroll_time(self):
        """Scroll the binary time across LEDs."""
        display.scroll(self.time_to_binary_string())


class MicrobitClockSystem:
    def __init__(self):
        self.clock = BinaryClock()

    def manual_setup(self):
        """Manual input for time and alarm via buttons."""
        # Set time
        display.scroll("SET HOUR")
        hour = self.get_number_input()
        display.scroll("SET MIN")
        minute = self.get_number_input()
        display.scroll("Set Seconds")
        seconds = self.get_number_input()
        self.clock.set_time(hour, minute, seconds)

        # Set alarm
        display.scroll("SET ALARM HOUR")
        alarm_hour = self.get_number_input()
        display.scroll("SET ALARM MIN")
        alarm_min = self.get_number_input()
        self.clock.set_alarm(alarm_hour, alarm_min)

    def get_number_input(self):
        """Get a number from 0–59 using buttons."""
        num = 0
        while True:
            display.show(num)

            #This is where you can set time & alarm time by clicking the A button on the microbit.
            if button_a.was_pressed():
                num = (num + 1) % 60
            #This is where you can confirm the A button dicision and move onto the next section.
            elif button_b.was_pressed():
                return num
            sleep(150)

    def run(self):
        """Main loop."""
        while True:
            self.clock.scroll_time()

            if self.clock.check_alarm():
                music.play(music.POWER_UP)

            sleep(1000)  # 1-second simulation
            self.clock.increment_time()


# Main Program
system = MicrobitClockSystem()
system.manual_setup()
system.run()