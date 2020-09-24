from urllib.request import urlretrieve
import os

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
if (os.path.isfile("local_copy.log") == False):
  print("Downloading local copy of log file...")
  local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))
  print("Download complete! Parsing log file...")
else:
  print("Local copy of log file found! Parsing log file...")


FILE_NAME = './local_copy.log'

import re
from datetime import datetime, timedelta, date
import calendar
from collections import Counter

last = 0
total = 0
mondays = 0
tuesdays = 0
wednesdays = 0
thursdays = 0
fridays = 0
saturdays = 0
sundays = 0
mon_count = 0
tue_count = 0
wed_count = 0
thu_count = 0
fri_count = 0
sat_count = 0
sun_count = 0
code_4xx = 0
code_3xx = 0
total_reqs = 0

files = {}
dates = {}

# split log_lines into [0:blank], [1: Date:Time], [2: Request Type], [3: file], [4: Protocol], [5: Return Code]
regex = re.compile(r".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?) (HTTP.*\"|\") ([2-5]0[0-9]) .*")

# Count number of requests in 1995
for line in open(FILE_NAME):
  repl = line.replace("[", "#", 10).replace(":", "#", 10).replace("/", "#", 10)
  year = repl.split('#')
  total += 1
  if len(year)>=3:
    if year[3] == str(1995):
        last += 1
 
 # Splits regex into elements
  elements = regex.split(line)
  # Bypasses short lines that cause errors
  if len(elements) < 3:
    continue
  # Extract the Date/Time in Element 1
  date = datetime.strptime(elements[1], "%d/%b/%Y")
  # Establish day of week based on date, and count number of requests per day of week
  weekday = date.isoweekday()
  if weekday == 1:
    mondays += 1
  if weekday == 2:
    tuesdays += 1
  if weekday == 3:
    wednesdays += 1
  if weekday == 4:
    thursdays += 1
  if weekday == 5:
    fridays += 1
  if weekday == 6:
    saturdays += 1
  if weekday == 7:
    sundays += 1

  # Counts the number of times each day of the week occurs in the log file
  days = elements[1]
  # If date is not logged in dictionary, adds date to dictionary
  if days in dates:
    continue
  else:
    dates[days] = 1

  # Calculates percentage of unsuccessful requests and redirected requests
  return_code = elements[6]
  total_reqs += 1
  if int(return_code) >= 400 and int(return_code) <= 499:
    code_4xx += 1
  if int(return_code) >= 300 and int(return_code) <= 399:
    code_3xx += 1
  
  # Creates a dictionary to track the number of times a file is requested
  filename = elements[4]
  # Checks elements[3] for new files or repeated files
  if filename in files:
    # Counts additional request of the file, if already added to dictionary
    files[filename] += 1
  # Counts the initial request of the file
  else:
    files[filename] = 1

# Extracts the First date and Last date from log file
first_date = date.strptime(list(dates.keys())[0], "%d/%b/%Y")
last_date = date.strptime(list(dates.keys())[-1], "%d/%b/%Y")

# Takes the keys from the Dates Dictionary and converts them to date objects
for k in dates:
  date_object = date.strptime(k, "%d/%b/%Y")
  day_of_week = date_object.isoweekday()
  # Increases counter for days of week
  if day_of_week == 1:
    mon_count += 1
  if day_of_week == 2:
    tue_count += 1
  if day_of_week == 3:
    wed_count += 1
  if day_of_week == 4:
    thu_count += 1
  if day_of_week == 5:
    fri_count += 1
  if day_of_week == 6:
    sat_count += 1
  if day_of_week == 7:
    sun_count += 1

# Divides total requests per week day and divides by number of times that weekday occured in the log
mon_avg = (mondays/mon_count)
tue_avg = (tuesdays/tue_count)
wed_avg = (wednesdays/wed_count)
thu_avg = (thursdays/thu_count)
fri_avg = (fridays/fri_count)
sat_avg = (saturdays/sat_count)
sun_avg = (sundays/sun_count)

# Isolates Month/Year from Days (element 1 as string)
month = days[3:]
for line in open(FILE_NAME):
  if month == "Oct/1994":
    Oct_94_ap = open("Oct_94.log", "a")
    Oct_94_ap.write(line)



# Converts Return Code totals to 35
perc_4xx = (code_4xx/total_reqs)*100
perc_3xx = (code_3xx/total_reqs)*100




print("There were ", last, "total requests made in the last year.")
print("There were ", total, "total requests made in the time period represented by the log.")
print("")
print("The total number of requests made on Mondays:", mondays)
print("The average number of requests made on Mondays:", mon_avg)
print("")
print("The total number of requests made on Tuesdays:", tuesdays)
print("The average number of requests made on Tuesdays:", tue_avg)
print("")
print("The total number of requests made on Wednesdays:", wednesdays)
print("The average number of requests made on Wednesdays:", wed_avg)
print("")
print("The total number of requests made on Thursdays:", thursdays)
print("The average number of requests made on Thursdays:", thu_avg)
print("")
print("The total number of requests made on Fridays:", fridays)
print("The average number of requests made on Fridays:", fri_avg)
print("")
print("The total number of requests made on Saturdays:", saturdays)
print("The average number of requests made on Saturdays:", sat_avg)
print("")
print("The total number of requests made on Sundays:", sundays)
print("The average number of requests made on Sundays:", sun_avg)
print("")
print("The percentage of redirected requests was", perc_3xx,)
print("The percentage of unsuccessful requests was", perc_4xx,)
print("")
print("The most requested file was:", sorted(files, key = files.get, reverse = True)[:1])
print("The least requested file was:", sorted(files, key = files.get, reverse = False)[:1])

print(month)