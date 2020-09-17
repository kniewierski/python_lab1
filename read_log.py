FILE_NAME = '/local_copy.log'

for line in open(FILE_NAME):
  line.split('[',']')
  print(line)