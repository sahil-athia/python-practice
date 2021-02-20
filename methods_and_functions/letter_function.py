# return a word with alternating capitals
def myfunc(word):
  final_word = ""
  counter = True
  for letter in word:
    if counter:
      counter = False
      final_word += letter.lower()
    else:
      counter = True
      final_word += letter.upper()
  return final_word

print myfunc("Anthropomorphism")