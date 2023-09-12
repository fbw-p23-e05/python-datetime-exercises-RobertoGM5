import datetime as dt

#Task 1

current_date = dt.datetime.now()
print("Current date and time:", current_date)
print("Current year:", current_date.year)
print("Month of year:", current_date.month)
print("Week number of the year:", current_date.strftime("%W"))
print("Weekday of the week:", current_date.strftime("%A"))
print("Day of year:", current_date.strftime("%j"))
print("Day of the month :", current_date.day)
print("Day of week:", current_date.strftime("%w"))

#Task 2

current_date = dt.datetime.now()
yesterday = current_date - dt.timedelta(days = 1)
tomorrow = current_date + dt.timedelta(days = 1)
print("Yesterday: ", yesterday.strftime("%Y-%m-%d"))
print("Today: ", current_date.strftime("%Y-%m-%d"))
print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))

#Task 3

current_date = dt.datetime.now()
add_five_sec = current_date + dt.timedelta(seconds = 5)
print("Current time:", current_date)
print("After adding 5 seconds:", add_five_sec)

#Task 4

current_date = dt.datetime.now()
print("Today:", current_date)
print("Next 5 days:")
for i in range(5):
    day_plus_one = current_date + dt.timedelta(days=i+1)
    print(day_plus_one)


#Task 5

current_date = dt.datetime.now()
print("Today:", current_date)
print("Day of year:", current_date.strftime("%j"))

#Task 6

current_date = dt.datetime.today()
if current_date.weekday() > 0:
    monday = current_date - dt.timedelta(days = current_date.weekday())
    print("The Monday of this week was:", monday.strftime("%Y-%m-%d"))
else:
    print("The Monday of this week is today:", current_date.strftime("%Y-%m-%d"))


#Task 7

year_input = int(input("Input a year: "))
current_date = dt.datetime(year_input, 1, 1)

print("Output:")
for i in range(365):
    if current_date.weekday() == 6:
        print(current_date.strftime("%Y-%m-%d"))
    current_date = current_date + dt.timedelta(days = 1)

