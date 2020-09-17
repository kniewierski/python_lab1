FILE_NAME = './local_copy.log'

for line in open(FILE_NAME):
  str.replace("[", "#")
  str.replace("/", "#")
  str.replace(":", "#")
  str.replace("]", "#")
  year = line.split('#',str)
  print(year)
