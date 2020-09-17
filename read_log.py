FILE_NAME = './local_copy.log'

for line in open(FILE_NAME):
  line.replace("[", "#", 10)
  line.replace("/", "#", 10)
  line.replace("]", "#", 10)
  year = line.split('#',str)
  print(year)
