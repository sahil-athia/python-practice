# anonymous function, implicit return following colon

square = lambda num: num ** 2
print square(3)

# used in conjunction with math and filter
my_nums = [1, 2, 3, 4, 5, 6]
names = ["eve", "salley", "john"]

# list all the squares
print list(map(lambda num: num ** 2, my_nums))

# only keep even numbers
print list(filter(lambda num: num % 2 == 0, my_nums))


# get the first letter in each name
print list(map(lambda name: name[0], names))

# reverse each name
print list(map(lambda name: name[::-1], names))