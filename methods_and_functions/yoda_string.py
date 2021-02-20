# return the reverse of a statement

def yoda(text):
  word_list = text.split()
  reverse_list = word_list[::-1]
  reversed_words = " ".join(reverse_list)
  return reversed_words

print yoda('I am home')
print yoda('We are ready')