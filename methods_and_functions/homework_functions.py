import math
import string

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


## multiply all number in a list
def multiply(nums):
  return map(lambda num: num * 2, nums)

print multiply([1, 2, 3, 4, 5, 6, 7])

## check is given word is a planidrome
def palindrome(text):
  return text == text[::-1]

print palindrome('helleh')
print palindrome('hellcvtequvybijeh')

## determine text is a pangram

def is_pangram(str1, alphabet = string.ascii_lowercase):
  ## remove spaces in text
  new_str = str1.replace(" ", "")

  ## create a list of unique lower case letter
  uniqe_str = list(set(new_str.lower()))

  ## make the list alphabetical
  uniqe_str.sort()

  ## make the list a string
  final_str = "".join(uniqe_str)
  
  return final_str in alphabet

print is_pangram("The quick brown fox jumps over the lazy dog")