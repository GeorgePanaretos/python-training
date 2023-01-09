#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# TODO: print today's date
now = datetime.now()
print("Today is", now)

# TODO: print today's date one year from now
print("One year from now:", str(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print("In 2 weeks and 3 days will be:", str(now + timedelta(weeks=2, days=3)))

# TODO: calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago was:", s)


# How many days until April Fools' Day?

today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year


# TODO: Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print("It's just", time_to_afd.days, "days until next April Fools' Day!")
