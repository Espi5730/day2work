# WRITE YOUR CODE HERE
import json
def compare(path1, path2):
  with open(path1) as file1:
    data1 = json.load(file1)

  with open(path2) as file2:
    data2 = json.load(file2)

  if data1 == data2:
    return 'The dictionaries are equal'

  if len(data1) > len(data2):
    return 'Dictionary 1 is longer than dictionary 2'
  elif len(data1) < len(data2):
    return 'Dictionary 2 is longer than dictionary 1'
  else:
    return 'Dictionary 1 and dictionary 2 have the same length'

# test code below
if __name__ == "__main__":
  import sys
  
  file1 = sys.argv[1]
  file2 = sys.argv[2]

  print(compare(file1, file2))