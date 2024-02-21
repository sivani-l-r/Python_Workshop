import datetime
import time

def set_alarm():
    print("Set the alarm time:")
    hours = int(input("Enter the hour (0-23): "))
    minutes = int(input("Enter the minute (0-59): "))
    return hours, minutes

# In Python, when you separate values by commas without enclosing them in square brackets [ ],
# parentheses ( ), or curly braces { }, Python interprets them as a tuple.

def check_alarm(current_time, alarm_time):
    return current_time.hour == alarm_time[0] and current_time.minute == alarm_time[1]

def alarm():
    print("Wake up! It's time!")


alarm_time = set_alarm() # go to set_alarm() function
print(alarm_time)
print("Alarm set for {}:{}.".format(alarm_time[0], alarm_time[1]))
# print("Alarm time",alarm_time[0],alarm_time[1])

while True:  # Enters into an infinite loop, where it continously checks the current time
    current_time = datetime.datetime.now()
    print("Current time:", current_time.strftime("%H:%M:%S"))

    if check_alarm(current_time, alarm_time):
        alarm()
        break

    time.sleep(1)  # Check every second


