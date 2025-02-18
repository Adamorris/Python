# imports the built in module - time
import time

# sets variable "duration" to 2 * 60
duration = 2 * 60

while duration:                                          # while duration is true
    # variable minutes, seconds = duration/60
    minutes, seconds = divmod(duration, 60)
    # sets the format for timer to be 00:00
    time_format = "{:02}:{:02}".format(minutes, seconds)
    # prints time format and makes every timer tick replace the current time at the beginning of the code of line
    print(time_format, end="\r")
    # sets the code to repeat every 1 seconds
    time.sleep(1)
    # duration - 1 (when 0 is reached the "while duration" is set to false which breaks the code)
    duration -= 1
# prints "time is up" signifying the end of the timer
print("time is up!")
