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

# split log_lines into [0:blank], [1: Date:Time], [2: Request Type], [3: file], [4: Protocol], [5: Return Code]
regex = re.compile(r".*\[([^:]*:.*) \-[0-9]{4}\] \"([A-Z]+) (.+?) (HTTP.*\"|\") ([2-5]0[0-9]) .*")

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
  date = datetime.strptime(elements[1], "%d/%b/%Y:%H:%M:%S")
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

  # Calculates percentage of unsuccessful requests and redirected requests
  return_code = elements[5]
  total_reqs += 1
  if int(return_code) >= 400 and int(return_code) <= 499:
    code_4xx += 1
  if int(return_code) >= 300 and int(return_code) <= 399:
    code_3xx += 1
  
  # Creates a dictionary to track the number of times a file is requested
  filename = elements[3]
  # Checks elements[3] for new files or repeated files
  if filename in files:
    # Counts additional request of the file, if already added to dictionary
    files[filename] += 1
  # Counts the initial request of the file
  else:
    files[filename] = 1

# Converts Return Code totals to Percentages
perc_4xx = (code_4xx/total_reqs)*100
perc_3xx = (code_3xx/total_reqs)*100

# Sorts the dictionary to choose the most requested file



print("There were ", last, "total requests made in the last year.")
print("There were ", total, "total requests made in the time period represented by the log.")
print("The total number of requests made on Mondays:", mondays)
print("The total number of requests made on Tuesdays:", tuesdays)
print("The total number of requests made on Wednesdays:", wednesdays)
print("The total number of requests made on Thursdays:", thursdays)
print("The total number of requests made on Fridays:", fridays)
print("The total number of requests made on Saturdays:", saturdays)
print("The total number of requests made on Sundays:", sundays)
print("The total number of unsuccessful requests was", code_4xx, ", resulting in", perc_4xx, "% of the total number of requests.")
print("The total number of redirected requests was", code_3xx, ", resulting in", perc_3xx, "% of the total number of requests.")

print("The most requested file was:", sorted(files, key = files.get, reverse = True)[:1])