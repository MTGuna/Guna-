import calendar
print("Month:",calendar.month(2016,12))
print("week:",calendar.leapdays(2000,2016))
print("week:",calendar.isleap(2016))
calendar.setfirstweekday(2)
print(calendar.month(2016,12))
print("Month:",calendar.weekday(2016,12,2))
