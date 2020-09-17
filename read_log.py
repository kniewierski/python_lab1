FILE_NAME = './local_copy.log'

for line in open(FILE_NAME):
  repl = line.replace("[", "#", 10).replace(":", "#", 10).replace("]", "#", 10)
  print(repl.split('#'))
  
