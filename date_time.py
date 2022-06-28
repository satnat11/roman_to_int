#date time in python
import datetime as dt

current_date =  dt.date.today()
print("current date: ",current_date)

new =  dt.date(2021,10,26)
print(new)
print("year: ",new.year)
print("month:",new.month)
print("day:",new.day)
print("_______________________________________________________")
a = dt.time(10,45,5,55502)
print(a)

print("______________________________________________________")

current_time=dt.datetime.now()
print("current time:",current_time)

print("_____________________________________________________")
new=dt.datetime(2021,5,31,12,2,56)
print(new)
print(new.date())
print(new.time())
print("_____________________________________________________")
current=dt.datetime.now()
new_year=dt.datetime(2023,1,1)
difference=new_year-current
print("difference is: ",difference)
print("_____________________________________________________")

current=dt.datetime.now()
print(current)
s=current.strftime("%A %B %d %Y")
print(s)
