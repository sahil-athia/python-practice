def even_check(number):
  return number % 2 == 0

print even_check(20)
print even_check(21)

# return true if any number ineven in a list
def check_even_list(num_list):
  even_numbers = []

  for number in num_list:
    if number % 2 == 0:
      even_numbers.append(number)
    else:
      pass
  return even_numbers


print check_even_list([1, 2, 3, 4, 5])
print check_even_list([1, 5, 3, 9, 5])
