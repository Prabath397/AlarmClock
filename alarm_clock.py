# Alarm Clock ⏰

import datetime
import time

print("⏰ Welcome to Alarm Clock!")

alarm_time = input("Enter alarm time (HH:MM, 24-hour format): ")

print(f"Alarm set for {alarm_time}...")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("⏰⏰ WAKE UP! Time's up! ⏰⏰")
        break
    time.sleep(1)
