# using range(start, stop, step)
for num in range(5):
  print num
print "-------------------"
for num in range(3, 5):
  print num
print "-------------------"
for num in range(0, 5, 2):
  print num

# we can store it in a list
list(range(5))

# enumaerate is used for index and elements
word = "abdce"

# this retuns tuples with the index count and element
for index, letter in enumerate(word):
  print index
  print letter
  print "\n"

# using zip
my_list = [1, 2, 3]
my_other_list = ["a", "b", "c"]

# gives us back a list of tuples, it matches up the 2 lists
# it only zips as far as it matches, if on list is 5 and one is 3 it will give 3 tuples 
for item in zip(my_list, my_other_list):
  print item

# use in for boolean check (inclusion), works on dictionaries
print "-------------------"
print "x" in [1, 2, 3]
print 1 in [1, 2, 3]

# math operators
numbers = [1, 2, 3, 4, 5, 6, 7]
print min(numbers)
print max(numbers)

# we are grabbing shuffle function from python
from random import shuffle
from random import randint 
shuffle(numbers)
print numbers
print randint(0, 100)

# we can ask users for input
result = input("give a number ")
type(result)
# int converts from string to number
print "this was your number: {}".format(int(result))