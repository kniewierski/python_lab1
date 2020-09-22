FILE_NAME = './local_copy.log'

import re
from datetime import date
from datetime import datetime

last = 0
total = 0
mondays = 0
tuesdays = 0
wednesdays = 0
thursdays = 0
fridays = 0
saturdays = 0
sundays = 0

regex = re.compile(r".*\[([^:]*:.*) \-[0-9]{4}\] \"([A-Z]+) (.+?) (HTTP.*\"|\") ([2-5]0[0-9]) .*")

for line in open(FILE_NAME):
  repl = line.replace("[", "#", 10).replace(":", "#", 10).replace("/", "#", 10)
  year = repl.split('#')
  total += 1
  if len(year)>=3:
    if year[3] == str(1995):
        last += 1
  elements = regex.split(line)
  if len(elements) < 3:
    continue
  date = datetime.strptime(elements[1], "%d/%b/%Y:%H:%M:%S")
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

print("There were ", last, "total requests made in the last year.")
print("There were ", total, "total requests made in the time period represented by the log.")
print("The total number of requests made on Mondays:", mondays)
print("The total number of requests made on Tuesdays:", tuesdays)
print("The total number of requests made on Wednesdays:", wednesdays)
print("The total number of requests made on Thursdays:", thursdays)
print("The total number of requests made on Fridays:", fridays)
print("The total number of requests made on Saturdays:", saturdays)
print("The total number of requests made on Sundays:", sundays)
