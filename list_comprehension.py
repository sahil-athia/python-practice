# alternative to using append wihtin a loop to create a list

my_string = "hello"

# one way of making a list out of this:
my_list = []
for letter in my_string:
  my_list.append(letter)

print my_list

# another way of doing the same code
my_list_comp = [letter for letter in my_string]
# the logic here is a flettened out for loop
# takes the element for each element in iterable data
print my_list_comp

#also useful for creating list out of nothing*
numbers_list = [x for x in range(10)]
print numbers_list

# we can also preform operaions on the first variable nme
numbers_list_new = [x**2 for x in range(10)]
print numbers_list_new

# lets also add some logic
even_list = [x for x in range(0, 10) if x % 2 == 0]
print even_list

# we can have else in this also (not good for readability)
even_odd = [x if x % 2 == 0 else "odd" for x in range(0, 10)]
print even_odd

# we can nest loops (not good for readability)
multiples = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
print multiples