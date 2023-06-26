### Module 6: Time (Problems 2-4) ###
import sys
import time
from datetime import datetime
from datetime import timedelta

# 2.  Add the timedelta to the datetime and subtract 60 seconds and add 2 years. (Hint: timedelta(seconds = 60)). For each condition, state the code and output.
current_date = datetime.now()
new_time = current_date - timedelta(seconds=60) + timedelta(weeks=104)

print(f"Current time: {current_date}")
print(f"New time: {new_time}\n")

# 3. Create a timedelta object representing 100 days, 10 hours, and 13 minutes.
object = timedelta(days=100, seconds=0, microseconds=0, milliseconds=0, minutes=13, hours=10)
print(object)
print("\n")

# 4. Write a function that takes two arguments (feet and inches) with this time object
feet = input("What is your height? First input your feet measurement. ")
inches = input("Now enter your inches measurement. ")

datetime_object = datetime.now()

def function(feet,inches):
    print(f"Today on {datetime_object} I am {feet} feet and {inches} inches tall.")

function(feet,inches)


