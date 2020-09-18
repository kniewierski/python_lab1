FILE_NAME = './local_copy.log'

from collections import Counter

last = 0
total = 0

for line in open(FILE_NAME):
  repl = line.replace("[", "#", 10).replace(":", "#", 10).replace("/", "#", 10)
  year = repl.split('#')[3]
  last = sum(1 for i in year if i == "1995")
  total = sum(1 for i in year)
  for i in year:
    print(i)
print("There were ", last, "total requests made in the last year.")
print("There were ", total, "total requests made in the time period represented by the log.")