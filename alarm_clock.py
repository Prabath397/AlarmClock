# Alarm Clock ⏰ with Cancel Option

import datetime
import time

print("⏰ Welcome to Alarm Clock!")

alarm_time = None

while True:
    if not alarm_time:
        alarm_time = input("\nEnter alarm time (HH:MM, 24-hour format): ")
        print(f"Alarm set for {alarm_time}...")
    else:
        choice = input("\nOptions: [C]ancel alarm, [Q]uit, or press Enter to continue: ").upper()

        if choice == "C":
            print("❌ Alarm cancelled.")
            alarm_time = None
            continue
        elif choice == "Q":
            print("👋 Goodbye!")
            break

    current_time = datetime.datetime.now().strftime("%H:%M")
    if alarm_time and current_time == alarm_time:
        print("⏰⏰ WAKE UP! Time's up! ⏰⏰")
        alarm_time = None  # reset alarm after ringing
    time.sleep(1)
