FILE_NAME = './local_copy.log'

for line in open(FILE_NAME):
  elements = line.split()
  year = elements.split('/')
  print(year)
