import math

## calculate sphere volume 

def volume(radius):
  return (4.0 / 3.0) * ((radius ** 3) * (math.pi))

print volume(2)

## check upper and lower clase letters
def upper_lower(text):
  number_upper = 0
  number_lower = 0
  for letter in text:
    if letter.isupper():
      number_upper += 1
    elif letter.islower():
      number_lower += 1
  return "{} upper case letter and {} lower case letter".format(number_upper, number_lower)
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print upper_lower(s)


## return uniqe list with no repetitives
def make_unique(data):
  return list(set(data))

print make_unique([1,1,1,1,2,2,3,3,3,3,4,5])