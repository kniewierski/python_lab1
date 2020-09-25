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


FILE_NAME = 'local_copy.log'

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
oct_94c = 0
nov_94c = 0
dec_94c = 0
jan_95c = 0
feb_95c = 0
mar_95c = 0
apr_95c = 0
may_95c = 0
jun_95c = 0
jul_95c = 0
aug_95c = 0
sep_95c = 0
oct_95c = 0


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
    
  
  # Counts the number of times each day of the week occurs in the log file
  days = elements[1]
  # If date is not logged in dictionary, adds date to dictionary
  if days in dates:
    continue
  else:
    dates[days] = 1
  
print("This file will take a while to parse, however will provide fantastic information for you!")

# Takes the keys from the Dates Dictionary and converts them to date objects
dates_list = list(dates.keys())
for i in dates_list:
  date_object = date.strptime(i, "%d/%b/%Y")
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


for line in open(FILE_NAME):
  # Counts number of requests per month and creates separate log file per month
  if "Oct/1994" in line:
    oct_94c += 1
    open("94_10-Oct94.txt", "a").writelines(line)

print("Right now, I'm splitting up the log file into much smaller files organized by month! Did you know the original file contained over 700,000 lines of code?")

for line in open(FILE_NAME):
  if "Nov/1994" in line:
    nov_94c += 1
    open("94_11-Nov94.txt", "a").writelines(line)

for line in open(FILE_NAME):
  if "Dec/1994" in line:
    dec_94c += 1
    open("94_12-Dec94.txt", "a").writelines(line)

for line in open(FILE_NAME):
  if "Jan/1995" in line:
    jan_95c += 1
    open("95_01-Jan95.txt", "a").writelines(line)

print("Fun fact: The Canary Islands are named after dogs, not birds!")

for line in open(FILE_NAME):
  if "Feb/1995" in line:
    feb_95c += 1
    open("95_02-Feb95.txt", "a").writelines(line)

for line in open(FILE_NAME):
  if "Mar/1995" in line:
    mar_95c += 1
    open("95_03-Mar95.txt", "a").writelines(line)

for line in open(FILE_NAME):
  if "Apr/1995" in line:
    apr_95c += 1
    open("95_04-Apr95.txt", "a").writelines(line)

print("Did you know? Canada has nine percent of the world's forests!")

for line in open(FILE_NAME):
  if "May/1995" in line:
    may_95c += 1
    open("95_05-May95.txt", "a").writelines(line)

for line in open(FILE_NAME):
  if "Jun/1995" in line:
    jun_95c += 1
    open("95_06-Jun95.txt", "a").writelines(line)

for line in open(FILE_NAME):
  if "Jul/1995" in line:
    jul_95c += 1
    open("95_07-Jul95.txt", "a").writelines(line)

print("Only 2 countries in the world have names that begin with \"The\", Can you guess them?")

for line in open(FILE_NAME):
  if "Aug/1995" in line:
    aug_95c += 1
    open("95_08-Aug95.txt", "a").writelines(line)

for line in open(FILE_NAME):
  if "Sep/1995" in line:
    sep_95c += 1
    open("95_09-Sep95.txt", "a").writelines(line)

print("If you thought the United States or the United Kingdom, you're incorrect. Believe it or not, the answers are: The Gambia and The Bahamas!")

for line in open(FILE_NAME):
  if "Oct/1995" in line:
    oct_95c += 1
    open("95_10-Oct95.txt", "a").writelines(line)


# Extracts the First date and Last date from log file
first_date = date.strptime(list(dates.keys())[0], "%d/%b/%Y")
last_date = date.strptime(list(dates.keys())[-1], "%d/%b/%Y")



# Divides total requests per week day and divides by number of times that weekday occured in the log
mon_avg = (mondays/mon_count)
tue_avg = (tuesdays/tue_count)
wed_avg = (wednesdays/wed_count)
thu_avg = (thursdays/thu_count)
fri_avg = (fridays/fri_count)
sat_avg = (saturdays/sat_count)
sun_avg = (sundays/sun_count)
# Average number of weeks in log period
week_avg = (mon_count + tue_count + wed_count + thu_count + fri_count + sat_count + sun_count)/7
# Converts Return Code totals to Percentages
perc_4xx = (code_4xx/total_reqs)*100
perc_3xx = (code_3xx/total_reqs)*100
# Average requests per week
req_week = total/week_avg

print("")
print("")
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
print("The average amount of requests per week:", req_week)
print("")
print("REQUESTS BY MONTH")
print("Q4'94: Oct -", oct_94c, "| Nov -", nov_94c, "| Dec -", dec_94c)
print("Q1'95: Jan -", jan_95c, "| Feb -", feb_95c, "| Mar -", mar_95c)
print("Q2'95: Apr -", apr_95c, "| May -", may_95c, "| Jun -", jun_95c)
print("Q3'95: Jul -", jul_95c, "| Aug -", aug_95c, "| Sep -", sep_95c)
print("Q4'95: Oct -", oct_95c)
print("*NOTE: Number of days in October '94 and '95 were less than the full month.*")
print("")
print("The most requested file was:", sorted(files, key = files.get, reverse = True)[:1])
print("The least requested file was:", sorted(files, key = files.get, reverse = False)[:1])
print("")