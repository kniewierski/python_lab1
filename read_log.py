FILE_NAME = './local_copy.log'

for line in open(FILE_NAME):
  year = line.split('[/:]',str)
  print(year)
