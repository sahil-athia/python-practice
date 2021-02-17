# syntax: iterable = [1, 2, 3]
#         for element in iterable:
#           print element

random_nums = [1, 4, 2, 5, 6, 3, 7]
random_string = "abcedfghijklmnop"
number_sum = 0

for number in random_nums:
  number_sum += number
  if number % 2 == 0:
    print ("even number: {}").format(number)
  else:
    print ("odd number: {}").format(number)

print number_sum

# when we dont intend to use the variable name inside of the loop
# use the _ as the placeholder: for _ in random_list: ...

# for letter in random_string:
  # print letter

my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

# we can replicate the structure of the tuples, its tuple unpacking
for a, b in my_list:
  print b


d = {"a": 1, "b": 2 }

# we can use a regular loop syntax for the keys, or get the pairs
for key, value in d.items():
  print key
  print value