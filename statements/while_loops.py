# syntax: while some_condition:
#           do something
x = 0

while x < 5:
  x += 1
  print "x is less than 5"
else:
  print "x is over 5"


# loops keywords: break: breaks out of the loop, continue: coes to the top of the closest enclosing loop
# pass: does nothing

y = [1, 2, 3]

# this will avoid the syntax error of having nothing in the loop
for item in y:
  pass

# using the continue keyword
letters = "abcdefghijklmnop"

for letter in letters:
  if letter == "b":
    continue
  print letter

print "---------------------------"
# using the break keyword
for letter in letters:
  if letter == "b":
    break
  print letter