# map requires a function and an iterable object (the function is only passed in not called)
# (function, interable) not (function(), iterable)
def square(number):
  return number ** 2

my_nums = [1, 2, 3, 4, 5]

# lets apply the square to all of the numbers in out list

for item in map(square, my_nums):
  print item

# if we want the list back, we can pass in list
print list(map(square, my_nums))


# try the map function with a slightly more complex function
def splicer(text):
  if len(text) % 2 == 0:
    return "EVEN"
  else:
    return text[0]
names = ["eve", "salley", "john"]

for name in map(splicer, names):
  print name