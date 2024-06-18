# WRITE YOUR CODE HERE
def is_nested(dict):
  values = dict.values()
  value_types = [type(elem) for elem in values]
  if type(()) in value_types or type([]) in value_types or type({}) in value_types:
    return True
  else:
    return False


# test code below
