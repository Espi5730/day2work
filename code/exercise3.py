# WRITE YOUR CODE HERE
def swap(dict):
  newdict = {}
  #for error check
  try:
    for key, value in dict.items():
      newdict[value] = key
  except TypeError:
    return 'Cannot swap the keys and values for this dictionary'

  return newdict

# test code below

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  swapped = swap(example_dict)
  print(swapped)

  # test code below
if __name__ == "__main__":
  example_dict = {
    1 : [2, 3],
    4 : 'four',
    5 : 'five'
  }

  swapped = swap(example_dict)
  print(swapped)

  # test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : {3 : 4},
    5 : 'five'
  }

  swapped = swap(example_dict)
  print(swapped)

  # test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : (4, 5)
  }

  swapped = swap(example_dict)
  print(swapped)