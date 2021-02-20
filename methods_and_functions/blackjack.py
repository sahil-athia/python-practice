def blackjack(a, b, c):
  if sum((a, b, c)) > 21:
    if 11 in (a, b, c):
      return sum((a, b, c)) - 10
    else:
      return "BUST"
  else:
    return sum((a, b + c))

print blackjack(5,6,7)
print blackjack(9,9,9)
print blackjack(9,9,11)