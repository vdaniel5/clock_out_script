from datetime import datetime, timedelta

# Input the clock-in time, clock-out for lunch time, and clock-in after lunch time
clock_in_time = input("Enter the clock-in time (HH:MM AM/PM): ")
clock_out_lunch_time = input("Enter the clock-out for lunch time (HH:MM AM/PM): ")
clock_in_after_lunch_time = input("Enter the clock-in after lunch time (HH:MM AM/PM): ")

# Convert the input times to datetime objects
format_str = "%I:%M %p"
clock_in = datetime.strptime(clock_in_time, format_str)
clock_out_lunch = datetime.strptime(clock_out_lunch_time, format_str)
clock_in_after_lunch = datetime.strptime(clock_in_after_lunch_time, format_str)

# Calculate the time worked before lunch
time_worked_before_lunch = clock_out_lunch - clock_in

# Calculate the remaining work duration
remaining_work_duration = timedelta(hours=8) - time_worked_before_lunch

# Calculate the clock-out time
clock_out_time = clock_in_after_lunch + remaining_work_duration

# Format the clock-out time for display
clock_out_time_formatted = clock_out_time.strftime(format_str)

print("You need to clock out at:", clock_out_time_formatted)

input("Press enter to exit")
