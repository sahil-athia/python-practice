# returns by a function that return by true or false
def check_even(num):
  return num % 2 == 0

my_nums = [1, 2, 3, 4, 5, 6]

for item in filter(check_even, my_nums):
  print item

even_nums = list(filter(check_even, my_nums))
print even_nums