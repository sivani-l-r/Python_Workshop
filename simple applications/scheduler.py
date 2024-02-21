import datetime

def add_event(schedule):
    event_name = input("Enter the event name: ")
    start_time = input("Enter the start time (HH:MM): ")
    end_time = input("Enter the end time (HH:MM): ")
    schedule.append((event_name, start_time, end_time))

def display_schedule(schedule):
    print("Scheduled Events for Today:")
    if not schedule:
        print("No events scheduled for today.")
    else:
        for event in schedule:
            print(f"{event[1]} - {event[2]}: {event[0]}")

def notify_event(schedule):
    current_time = datetime.datetime.now().strftime("%H:%M")
    for event in schedule:
        if event[1] <= current_time < event[2]:
            print(f"It's time for '{event[0]}'!")
            break


schedule = []
while True:

    print("\nEvent Scheduler Menu:")
    print("1. Add Event")
    print("2. View Schedule")
    print("3. Check for Current Event")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_event(schedule)
    elif choice == '2':
        display_schedule(schedule)
    elif choice == '3':
        notify_event(schedule)
    elif choice == '4':
        print("Exiting Event Scheduler. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

