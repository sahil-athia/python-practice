# if the passed in words start with the same letter return true

def double_l(text):
  words = text.split()
  return words[0][0] == words[1][0]

print double_l('Levelheaded Llama')
print double_l('Crazy Kangaroo') 