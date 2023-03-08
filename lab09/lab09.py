
import random
import statistics

def wordcount(fname):
  try:
    file = open(fname, "r")
    file_string = file.read()
    split = file_string.split()
    print(len(split))
  except FileNotFoundError:
    print("No such file or directory: " + fname)

def make_data(fname):
  file = open(fname, "w")
  for i in range(1000):
    line = str(i+1) + ", " + str(random.randint(-1000, 1000)) + "\n"
    file.write(line)
  file.close()
  return file

def read_file(fname):
  try:
    file = open(fname, "r")
    file_string = file.read()
    file_string = file_string.split("\n")
    for i in range(len(file_string)):
      s = file_string[i]
      x = s.find(",")
      s = s[x+2:]
      file_string[i] = s
    file_string.pop(-1)
    for i in range(len(file_string)):
      file_string[i] = int(file_string[i])
    print("maximum value: " + str(max(file_string)))
    print("minimum value: " + str(min(file_string)))
  except FileNotFoundError:
    print("No such file or directory: " + fname)

def stock(fname):
  file = open(fname, "r")
  file_string = file.read()
  file_string = file_string.split("\n")
  
  for i in range(len(file_string)):
    for j in range(4):
      s = file_string[i]
      x = s.find(",")
      s = s[x+1:]
      file_string[i] = s
    s = file_string[i]
    x = s.find(",")
    s = s[:x]
    file_string[i] = s
  file_string.pop(0)
  for i in range(len(file_string)):
      file_string[i] = float(file_string[i])
  print("maximum value: " + str(max(file_string)))
  print("minimum value: " + str(min(file_string)))
  print("mean value: " + str(statistics.mean(file_string)))
  print("median value: " + str(statistics.median(file_string)))
  return
