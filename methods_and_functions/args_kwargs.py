# these are functional paramaters
# *args and **kwargs are arguments and key word arguments

def my_func(a,b):
  # return 5% of the sum of a and b
  return sum((a, b)) * 0.05

print my_func(40, 60)

# if we didnt want to conform to just 2 or any fixed number of arguments we use this:

def new_func(*args):
  # this will cause all of the parameters passed in to default into a tuple
  # the word also doesnt have to be "args", we can say *stuff
  return sum(args) * 0.05

print new_func(40, 60, 100, 90, 10)