FILE_NAME = './local_copy.log'

import re
from datetime import date
from datetime import datetime

ERRORS = []

last = 0
total = 0
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
print(elements)
print("There were ", last, "total requests made in the last year.")
print("There were ", total, "total requests made in the time period represented by the log.")

mon1 = datetime.strptime("09/Oct/1995:00:00:00", "%d/%b/%Y:%H:%M:%S")
tue1 = datetime.strptime("10/Oct/1995:00:00:00", "%d/%b/%Y:%H:%M:%S")
wed1 = datetime.strptime("11/Oct/1995:00:00:00", "%d/%b/%Y:%H:%M:%S")
thu1 = datetime.strptime("05/Oct/1995:00:00:00", "%d/%b/%Y:%H:%M:%S")
fri1 = datetime.strptime("06/Oct/1995:00:00:00", "%d/%b/%Y:%H:%M:%S")
sat1 = datetime.strptime("07/Oct/1995:00:00:00", "%d/%b/%Y:%H:%M:%S")
sun1 = datetime.strptime("08/Oct/1995:00:00:00", "%d/%b/%Y:%H:%M:%S")

mondays = 1
tuesdays = 1
wednesdays = 1
thursdays = 1
fridays = 1
saturdays = 1
sundays = 1

mon_delta = mon1 - date
tue_delta = tue1 - date
wed_delta = wed1 - date
thu_delta = thu1 - date
fri_delta = fri1 - date
sat_delta = sat1 - date
sun_delta = sun1 - date

for line in open(FILE_NAME):
    if mon_delta/7 == range(1, 750000, 1):
      mondays += 1
    if tue_delta/7 == range(1,750000, 1):
      tuesdays += 1
    if wed_delta/7 == range(1, 750000, 1):
      wednesdays += 1
    if thu_delta/7 == range(1,750000, 1):
      thursdays += 1
    if fri_delta/7 == range(1,750000, 1):
      fridays += 1
    if sat_delta/7 == range(1,750000, 1):
      saturdays += 1
    if sun_delta/7 == range(1,750000, 1):
      sundays += 1

print("The total number of requests made on Mondays:", mondays)
print("The total number of requests made on Tuesdays:", tuesdays)
print("The total number of requests made on Wednesdays:", wednesdays)
print("The total number of requests made on Thursdays:", thursdays)
print("The total number of requests made on Fridays:", fridays)
print("The total number of requests made on Saturdays:", saturdays)
print("The total number of requests made on Sundays:", sundays)
