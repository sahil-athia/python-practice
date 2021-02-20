def count_primes(num):

  # check for 0 or 1 input
  if num < 2:
    return 0
  
  # store our prime numbers
  primes = [2]
  # counter upto input number ()
  x = 3

  while x <= num:
    # for the numbers between 3 and out counter, skipping by 2 since even numbers are not prime
    for y in range(3, x, 2):
      # this determine when we DONT have a prime number
      if x % y == 0:
        x += 2
        break
    else:
      # this else state that if we dont break out of our for loop
      primes.append(x)
      x += 2

  return primes, len(primes)

print count_primes(100)