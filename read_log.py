FILE_NAME = './local_copy.log'

from collections import Counter

for line in open(FILE_NAME):
  repl = line.replace("[", "#", 10).replace(":", "#", 10).replace("/", "#", 10)
  spl = repl.split('#')
  last = sum(1 for i in spl if i == "1995")
  print("There were ", last, "total requests made in the last year.")
  total = sum(1 for i in spl)
  print("There were ", total, "total requests made in the time period represented by the log.")