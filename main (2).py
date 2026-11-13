import calendar

Event = input("Enter event title: ")
Year = int(input("Enter year: "))
Month = int(input("Enter month: "))
Day = int(input("Enter day: "))
Complete_date = f"{calendar.month_name[Month]} {Day}, {Year}"

print()
   
print(f"Event: {Event}")
print(f"Date: {Complete_date}")
print(f"Year: {Year}")
print(f"Month: {calendar.month_name[Month]}")
print(f"Day: {Day}")
