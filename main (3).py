import calendar

#USER INPUT
Event = input("Enter event title: ")
Year = int(input("Enter year: "))
Month = int(input("Enter month: "))
Day = int(input("Enter day: "))
Date = f"{Month} {Day}, {Year}"

#DATE FORMATTER AREA 
Complete_date = f"{calendar.month_name[Month]} {Day}, {Year}"
weekday = calendar.weekday(Year, Month, Day)
weekday_name = calendar.day_name[weekday]

print()

#DISPLAY
print(f"Event: {Event.upper()}")
print(f"Date: {Complete_date}")
print(f"Year: {Year}")
print(f"Month: {calendar.month_name[Month]}")
print(f"Day: {Day}")
print(f"Weekday: {weekday_name}")

