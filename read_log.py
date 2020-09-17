FILE_NAME = './local_copy.log'

from collections import Counter

for line in open(FILE_NAME):
  repl = line.replace("[", "#", 10).replace(":", "#", 10).replace("/", "#", 10)
  year = repl.split('#')
  print(year[3])