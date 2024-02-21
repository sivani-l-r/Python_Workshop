import datetime

def add_event(schedule):
    time = input("Enter the time for the event (format HH:MM): ")
    event = input("Enter the event: ")
    schedule[time] = event

def display_schedule(schedule):
    print("Daily Schedule:")
    for time, event in sorted(schedule.items()):
        print(f"{time}: {event}")

def main():
    schedule = {}
    while True:
        print("\nDaily Planner Menu:")
        print("1. Add Event")
        print("2. View Schedule")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_event(schedule)
        elif choice == '2':
            display_schedule(schedule)
        elif choice == '3':
            print("Exiting Daily Planner. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
