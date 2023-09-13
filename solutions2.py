import datetime as dt

#Task 1

current_date = dt.datetime.now()
substract_15days = current_date - dt.timedelta(days = 15)
print(substract_15days.strftime('%Y-%m-%d'))

#Task 2

current_date = dt.datetime.now()
add_7days = current_date + dt.timedelta(days = 7)
print(add_7days.strftime('%Y-%m-%d'))

#Task 3

current_date = dt.datetime(year=2020, month=1, day=1)
current_date += dt.timedelta(days = 25)
print(f"Hello Friedrich, your rent of 300 € is due on {current_date.strftime('%d %B, %Y')}.")

